-- Art Culinary CRM
-- PostgreSQL: хранимые функции, процедура и триггеры

CREATE OR REPLACE FUNCTION crm_recalculate_order_total(p_order_id BIGINT)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    v_total NUMERIC;
BEGIN
    SELECT COALESCE(SUM(line_total), 0)
      INTO v_total
      FROM crm_orderitem
     WHERE order_id = p_order_id;

    UPDATE crm_order
       SET total_amount = v_total
     WHERE id = p_order_id;

    RETURN v_total;
END;
$$;

CREATE OR REPLACE FUNCTION crm_tg_validate_delivery_date()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.delivery_date IS NOT NULL AND NEW.delivery_date < CURRENT_DATE THEN
        RAISE EXCEPTION 'delivery_date (%) cannot be in the past', NEW.delivery_date;
    END IF;
    RETURN NEW;
END;
$$;

CREATE OR REPLACE FUNCTION crm_tg_prepare_orderitem()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.quantity <= 0 THEN
        RAISE EXCEPTION 'quantity must be greater than 0';
    END IF;
    IF NEW.unit_price < 0 THEN
        RAISE EXCEPTION 'unit_price cannot be negative';
    END IF;
    NEW.line_total := ROUND(NEW.quantity * NEW.unit_price, 2);
    RETURN NEW;
END;
$$;

CREATE OR REPLACE FUNCTION crm_tg_orderitem_total_recalc()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        PERFORM crm_recalculate_order_total(OLD.order_id);
    ELSE
        PERFORM crm_recalculate_order_total(NEW.order_id);
    END IF;
    RETURN NULL;
END;
$$;

CREATE OR REPLACE FUNCTION crm_tg_check_ingredient_reservation()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_reserved NUMERIC;
    v_stock NUMERIC;
BEGIN
    SELECT COALESCE(SUM(quantity), 0)
      INTO v_reserved
      FROM crm_ingredientreservation
     WHERE ingredient_id = NEW.ingredient_id
       AND production_date = NEW.production_date
       AND id <> COALESCE(NEW.id, -1);

    SELECT COALESCE(quantity, 0)
      INTO v_stock
      FROM crm_ingredientstock
     WHERE ingredient_id = NEW.ingredient_id;

    IF (v_reserved + NEW.quantity) > v_stock THEN
        RAISE EXCEPTION 'insufficient ingredient stock for ingredient_id=% and production_date=%',
            NEW.ingredient_id, NEW.production_date;
    END IF;

    RETURN NEW;
END;
$$;

CREATE OR REPLACE PROCEDURE crm_set_order_status(
    p_order_id BIGINT,
    p_status VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE crm_order
       SET status = p_status,
           updated_at = NOW()
     WHERE id = p_order_id;
END;
$$;

DROP TRIGGER IF EXISTS trg_crm_order_validate_delivery_date ON crm_order;
CREATE TRIGGER trg_crm_order_validate_delivery_date
BEFORE INSERT OR UPDATE OF delivery_date ON crm_order
FOR EACH ROW
EXECUTE FUNCTION crm_tg_validate_delivery_date();

DROP TRIGGER IF EXISTS trg_crm_orderitem_prepare ON crm_orderitem;
CREATE TRIGGER trg_crm_orderitem_prepare
BEFORE INSERT OR UPDATE OF quantity, unit_price ON crm_orderitem
FOR EACH ROW
EXECUTE FUNCTION crm_tg_prepare_orderitem();

DROP TRIGGER IF EXISTS trg_crm_orderitem_total_recalc ON crm_orderitem;
CREATE TRIGGER trg_crm_orderitem_total_recalc
AFTER INSERT OR UPDATE OR DELETE ON crm_orderitem
FOR EACH ROW
EXECUTE FUNCTION crm_tg_orderitem_total_recalc();

DROP TRIGGER IF EXISTS trg_crm_ingredientreservation_check ON crm_ingredientreservation;
CREATE TRIGGER trg_crm_ingredientreservation_check
BEFORE INSERT OR UPDATE OF quantity, ingredient_id, production_date ON crm_ingredientreservation
FOR EACH ROW
EXECUTE FUNCTION crm_tg_check_ingredient_reservation();
