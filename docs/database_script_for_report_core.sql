-- Скрипт предметной БД Art Culinary CRM (ядро домена, SQLite)
PRAGMA foreign_keys = ON;

-- TABLE: admin_panel_backup
CREATE TABLE "admin_panel_backup" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "file_path" varchar(255) NOT NULL, "status" varchar(20) NOT NULL, "created_at" datetime NOT NULL, "created_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: admin_panel_backupschedule
CREATE TABLE "admin_panel_backupschedule" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "frequency" varchar(20) NOT NULL, "is_active" bool NOT NULL, "updated_at" datetime NOT NULL);

-- TABLE: crm_auditlog
CREATE TABLE "crm_auditlog" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "actor_role" varchar(64) NOT NULL, "object_type" varchar(64) NOT NULL, "object_id" integer unsigned NOT NULL CHECK ("object_id" >= 0), "field_name" varchar(64) NOT NULL, "old_value" text NOT NULL, "new_value" text NOT NULL, "reason" text NOT NULL, "created_at" datetime NOT NULL, "actor_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_client
CREATE TABLE "crm_client" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "client_type" varchar(32) NOT NULL, "inn" varchar(20) NOT NULL, "kpp" varchar(20) NOT NULL, "default_delivery_address" varchar(255) NOT NULL, "email" varchar(254) NOT NULL, "phone" varchar(32) NOT NULL, "status" varchar(20) NOT NULL, "responsible_manager_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "current_stage_id" bigint NULL REFERENCES "crm_cooperationstage" ("id") DEFERRABLE INITIALLY DEFERRED, "created_at" datetime NULL, "daily_max_weight_kg" decimal NULL, "daily_min_qty" decimal NULL, "guaranteed_volume_kg" decimal NULL);

-- TABLE: crm_clientallowedtechcard
CREATE TABLE "crm_clientallowedtechcard" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "client_id" bigint NOT NULL REFERENCES "crm_client" ("id") DEFERRABLE INITIALLY DEFERRED, "tech_card_id" bigint NOT NULL REFERENCES "crm_techcard" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_clientcontact
CREATE TABLE "crm_clientcontact" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "full_name" varchar(255) NOT NULL, "position" varchar(128) NOT NULL, "phone" varchar(32) NOT NULL, "email" varchar(254) NOT NULL, "is_primary" bool NOT NULL, "client_id" bigint NOT NULL REFERENCES "crm_client" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_clientstagehistory
CREATE TABLE "crm_clientstagehistory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "changed_at" datetime NOT NULL, "comment" text NOT NULL, "changed_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "client_id" bigint NOT NULL REFERENCES "crm_client" ("id") DEFERRABLE INITIALLY DEFERRED, "stage_id" bigint NULL REFERENCES "crm_cooperationstage" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_cooperationstage
CREATE TABLE "crm_cooperationstage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "order" smallint unsigned NOT NULL CHECK ("order" >= 0), "is_active" bool NOT NULL);

-- TABLE: crm_courier
CREATE TABLE "crm_courier" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "transport_type" varchar(64) NOT NULL, "experience_years" smallint unsigned NOT NULL CHECK ("experience_years" >= 0), "user_id" bigint NOT NULL UNIQUE REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "zone" varchar(128) NOT NULL, "payload_capacity_kg" decimal NULL, "cargo_volume_m3" decimal NULL, "cargo_length_cm" decimal NULL, "cargo_width_cm" decimal NULL, "cargo_height_cm" decimal NULL, "current_lat" decimal NULL, "current_lng" decimal NULL, "location_updated_at" datetime NULL, "current_latitude" decimal NULL, "current_longitude" decimal NULL, "max_volume" decimal NULL, "max_weight" decimal NULL, "status" varchar(20) NOT NULL);

-- TABLE: crm_courierassignment
CREATE TABLE "crm_courierassignment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "assigned_at" datetime NOT NULL, "courier_id" bigint NOT NULL REFERENCES "crm_courier" ("id") DEFERRABLE INITIALLY DEFERRED, "route_id" bigint NOT NULL REFERENCES "crm_route" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_delivery
CREATE TABLE "crm_delivery" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "departure_time" datetime NULL, "delivered_at" datetime NULL, "address" varchar(255) NOT NULL, "note" text NOT NULL, "is_sent" bool NOT NULL, "courier_id" bigint NULL REFERENCES "crm_courier" ("id") DEFERRABLE INITIALLY DEFERRED, "order_id" bigint NOT NULL REFERENCES "crm_order" ("id") DEFERRABLE INITIALLY DEFERRED, "planned_at" datetime NULL, "route_id" bigint NULL REFERENCES "crm_route" ("id") DEFERRABLE INITIALLY DEFERRED, "cargo_weight_kg" decimal NULL, "cargo_volume_m3" decimal NULL, "cargo_length_cm" decimal NULL, "cargo_width_cm" decimal NULL, "cargo_height_cm" decimal NULL, "delivery_date" date NULL, "status" varchar(20) NOT NULL);

-- TABLE: crm_dish
CREATE TABLE "crm_dish" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "unit" varchar(32) NOT NULL, "is_active" bool NOT NULL, "created_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "batch_multiple_qty" decimal NULL, "min_batch_qty" decimal NULL, "unit_weight_kg" decimal NULL, "default_price" decimal NULL, "daily_capacity" decimal NULL, "base_uom" varchar(8) NOT NULL, "quantity_scale" smallint unsigned NOT NULL CHECK ("quantity_scale" >= 0));

-- TABLE: crm_dishequipmentrequirement
CREATE TABLE "crm_dishequipmentrequirement" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "minutes_per_unit" decimal NOT NULL, "dish_id" bigint NOT NULL REFERENCES "crm_dish" ("id") DEFERRABLE INITIALLY DEFERRED, "equipment_id" bigint NOT NULL REFERENCES "crm_equipment" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_equipment
CREATE TABLE "crm_equipment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "capacity_per_hour" decimal NULL, "available_hours" decimal NULL);

-- TABLE: crm_equipmentreservation
CREATE TABLE "crm_equipmentreservation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "production_date" date NOT NULL, "hours" decimal NOT NULL, "equipment_id" bigint NOT NULL REFERENCES "crm_equipment" ("id") DEFERRABLE INITIALLY DEFERRED, "order_id" bigint NOT NULL REFERENCES "crm_order" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_ingredient
CREATE TABLE "crm_ingredient" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE, "is_active" bool NOT NULL);

-- TABLE: crm_ingredientreservation
CREATE TABLE "crm_ingredientreservation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "production_date" date NOT NULL, "quantity" decimal NOT NULL, "ingredient_id" bigint NOT NULL REFERENCES "crm_ingredient" ("id") DEFERRABLE INITIALLY DEFERRED, "order_id" bigint NOT NULL REFERENCES "crm_order" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_ingredientstock
CREATE TABLE "crm_ingredientstock" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" decimal NOT NULL, "ingredient_id" bigint NOT NULL UNIQUE REFERENCES "crm_ingredient" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_interaction
CREATE TABLE "crm_interaction" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "interaction_type" varchar(20) NOT NULL, "note" text NOT NULL, "happened_at" datetime NOT NULL, "client_id" bigint NOT NULL REFERENCES "crm_client" ("id") DEFERRABLE INITIALLY DEFERRED, "manager_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_logisticianprofile
CREATE TABLE "crm_logisticianprofile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "region" varchar(128) NOT NULL, "city" varchar(128) NOT NULL, "transport_types" text NOT NULL CHECK ((JSON_VALID("transport_types") OR "transport_types" IS NULL)), "timezone" varchar(64) NOT NULL, "map_show_traffic" bool NOT NULL, "user_id" bigint NOT NULL UNIQUE REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "preferred_route_type" varchar(16) NOT NULL);

-- TABLE: crm_order
CREATE TABLE "crm_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_number" varchar(50) NOT NULL UNIQUE, "address" varchar(255) NOT NULL, "comments" text NOT NULL, "total_amount" decimal NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "client_id" bigint NOT NULL REFERENCES "crm_client" ("id") DEFERRABLE INITIALLY DEFERRED, "manager_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "is_archived" bool NOT NULL, "delivery_date" date NULL, "delivery_time" time NULL, "delivery_type" varchar(32) NOT NULL, "production_date" date NULL, "production_shift" varchar(32) NOT NULL, "production_window_end" time NULL, "production_window_start" time NULL, "status" varchar(64) NOT NULL);

-- TABLE: crm_orderitem
CREATE TABLE "crm_orderitem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" decimal NOT NULL, "unit_price" decimal NOT NULL, "line_total" decimal NOT NULL, "supply_type" varchar(64) NOT NULL, "dish_id" bigint NULL REFERENCES "crm_dish" ("id") DEFERRABLE INITIALLY DEFERRED, "ingredient_id" bigint NULL REFERENCES "crm_ingredient" ("id") DEFERRABLE INITIALLY DEFERRED, "order_id" bigint NOT NULL REFERENCES "crm_order" ("id") DEFERRABLE INITIALLY DEFERRED, "custom_tech_card_id" bigint NULL REFERENCES "crm_techcard" ("id") DEFERRABLE INITIALLY DEFERRED, "picked_quantity" decimal NOT NULL, "item_status" varchar(20) NOT NULL, "item_comment" varchar(255) NOT NULL, "replacement_text" varchar(255) NOT NULL);

-- TABLE: crm_pickingsession
CREATE TABLE "crm_pickingsession" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "note" text NOT NULL, "started_at" datetime NULL, "finished_at" datetime NULL, "updated_at" datetime NOT NULL, "order_id" bigint NOT NULL UNIQUE REFERENCES "crm_order" ("id") DEFERRABLE INITIALLY DEFERRED, "picker_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_productionreservation
CREATE TABLE "crm_productionreservation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "production_date" date NOT NULL, "weight_kg" decimal NOT NULL, "order_id" bigint NOT NULL REFERENCES "crm_order" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_role
CREATE TABLE "crm_role" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL UNIQUE);

-- TABLE: crm_route
CREATE TABLE "crm_route" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "planned_date" date NOT NULL, "notes" text NOT NULL, "logistician_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "max_duration_minutes" smallint unsigned NOT NULL CHECK ("max_duration_minutes" >= 0), "soft_limit_stops" smallint unsigned NOT NULL CHECK ("soft_limit_stops" >= 0), "strict_mode" bool NOT NULL, "status" varchar(20) NOT NULL);

-- TABLE: crm_routestop
CREATE TABLE "crm_routestop" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "sequence_index" smallint unsigned NOT NULL CHECK ("sequence_index" >= 0), "planned_time" datetime NULL, "actual_time" datetime NULL, "note" varchar(255) NOT NULL, "delivery_id" bigint NOT NULL REFERENCES "crm_delivery" ("id") DEFERRABLE INITIALLY DEFERRED, "route_id" bigint NOT NULL REFERENCES "crm_route" ("id") DEFERRABLE INITIALLY DEFERRED, "latitude" decimal NULL, "longitude" decimal NULL, "status" varchar(20) NOT NULL, "delivery_date" date NULL, "failure_reason" text NOT NULL, "proof_of_delivery" varchar(100) NULL, "proof_uploaded_at" datetime NULL, "proof_uploaded_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "service_time_minutes" smallint unsigned NOT NULL CHECK ("service_time_minutes" >= 0), "proof_review_comment" text NOT NULL, "proof_review_status" varchar(32) NOT NULL, "proof_reviewed_at" datetime NULL, "proof_reviewed_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_techcard
CREATE TABLE "crm_techcard" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "version_label" varchar(32) NOT NULL, "description" text NOT NULL, "photo_url" varchar(200) NOT NULL, "is_active" bool NOT NULL, "approved_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "dish_id" bigint NOT NULL REFERENCES "crm_dish" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_techcardcomponent
CREATE TABLE "crm_techcardcomponent" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" decimal NOT NULL, "note" varchar(255) NOT NULL, "ingredient_id" bigint NOT NULL REFERENCES "crm_ingredient" ("id") DEFERRABLE INITIALLY DEFERRED, "tech_card_id" bigint NOT NULL REFERENCES "crm_techcard" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_techcardvariant
CREATE TABLE "crm_techcardvariant" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" decimal NOT NULL, "note" varchar(255) NOT NULL, "tech_card_id" bigint NOT NULL REFERENCES "crm_techcard" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_user
CREATE TABLE "crm_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "full_name" varchar(255) NOT NULL, "phone" varchar(32) NOT NULL);

-- TABLE: crm_user_groups
CREATE TABLE "crm_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_user_user_permissions
CREATE TABLE "crm_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: crm_userrole
CREATE TABLE "crm_userrole" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "assigned_at" datetime NOT NULL, "role_id" bigint NOT NULL REFERENCES "crm_role" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- TABLE: reports_report
CREATE TABLE "reports_report" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "period_from" date NOT NULL, "period_to" date NOT NULL, "status" varchar(20) NOT NULL, "file" varchar(100) NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "created_by_id" bigint NULL REFERENCES "crm_user" ("id") DEFERRABLE INITIALLY DEFERRED, "validation_status" varchar(20) NOT NULL, "validation_message" text NOT NULL);

-- INDEX: admin_panel_backup_created_by_id_f9e87668
CREATE INDEX "admin_panel_backup_created_by_id_f9e87668" ON "admin_panel_backup" ("created_by_id");

-- INDEX: crm_auditlog_actor_id_4382924f
CREATE INDEX "crm_auditlog_actor_id_4382924f" ON "crm_auditlog" ("actor_id");

-- INDEX: crm_client_current_stage_id_e8a55701
CREATE INDEX "crm_client_current_stage_id_e8a55701" ON "crm_client" ("current_stage_id");

-- INDEX: crm_client_responsible_manager_id_7081e9b4
CREATE INDEX "crm_client_responsible_manager_id_7081e9b4" ON "crm_client" ("responsible_manager_id");

-- INDEX: crm_clientallowedtechcard_client_id_a202bbc1
CREATE INDEX "crm_clientallowedtechcard_client_id_a202bbc1" ON "crm_clientallowedtechcard" ("client_id");

-- INDEX: crm_clientallowedtechcard_client_id_tech_card_id_f1bfd130_uniq
CREATE UNIQUE INDEX "crm_clientallowedtechcard_client_id_tech_card_id_f1bfd130_uniq" ON "crm_clientallowedtechcard" ("client_id", "tech_card_id");

-- INDEX: crm_clientallowedtechcard_tech_card_id_4956fc6d
CREATE INDEX "crm_clientallowedtechcard_tech_card_id_4956fc6d" ON "crm_clientallowedtechcard" ("tech_card_id");

-- INDEX: crm_clientcontact_client_id_b44e105e
CREATE INDEX "crm_clientcontact_client_id_b44e105e" ON "crm_clientcontact" ("client_id");

-- INDEX: crm_clientstagehistory_changed_by_id_84f6d086
CREATE INDEX "crm_clientstagehistory_changed_by_id_84f6d086" ON "crm_clientstagehistory" ("changed_by_id");

-- INDEX: crm_clientstagehistory_client_id_926d0169
CREATE INDEX "crm_clientstagehistory_client_id_926d0169" ON "crm_clientstagehistory" ("client_id");

-- INDEX: crm_clientstagehistory_stage_id_04e1997a
CREATE INDEX "crm_clientstagehistory_stage_id_04e1997a" ON "crm_clientstagehistory" ("stage_id");

-- INDEX: crm_courierassignment_courier_id_d66fb584
CREATE INDEX "crm_courierassignment_courier_id_d66fb584" ON "crm_courierassignment" ("courier_id");

-- INDEX: crm_courierassignment_courier_id_route_id_4ca14639_uniq
CREATE UNIQUE INDEX "crm_courierassignment_courier_id_route_id_4ca14639_uniq" ON "crm_courierassignment" ("courier_id", "route_id");

-- INDEX: crm_courierassignment_route_id_40d05eac
CREATE INDEX "crm_courierassignment_route_id_40d05eac" ON "crm_courierassignment" ("route_id");

-- INDEX: crm_delivery_courier_id_fa676b65
CREATE INDEX "crm_delivery_courier_id_fa676b65" ON "crm_delivery" ("courier_id");

-- INDEX: crm_delivery_order_id_88ce6731
CREATE INDEX "crm_delivery_order_id_88ce6731" ON "crm_delivery" ("order_id");

-- INDEX: crm_delivery_route_id_7a215b73
CREATE INDEX "crm_delivery_route_id_7a215b73" ON "crm_delivery" ("route_id");

-- INDEX: crm_dish_created_by_id_1ec5aa20
CREATE INDEX "crm_dish_created_by_id_1ec5aa20" ON "crm_dish" ("created_by_id");

-- INDEX: crm_dishequipmentrequirement_dish_id_d09c1cdf
CREATE INDEX "crm_dishequipmentrequirement_dish_id_d09c1cdf" ON "crm_dishequipmentrequirement" ("dish_id");

-- INDEX: crm_dishequipmentrequirement_dish_id_equipment_id_03d5c14f_uniq
CREATE UNIQUE INDEX "crm_dishequipmentrequirement_dish_id_equipment_id_03d5c14f_uniq" ON "crm_dishequipmentrequirement" ("dish_id", "equipment_id");

-- INDEX: crm_dishequipmentrequirement_equipment_id_c03741cd
CREATE INDEX "crm_dishequipmentrequirement_equipment_id_c03741cd" ON "crm_dishequipmentrequirement" ("equipment_id");

-- INDEX: crm_equipmentreservation_equipment_id_01460725
CREATE INDEX "crm_equipmentreservation_equipment_id_01460725" ON "crm_equipmentreservation" ("equipment_id");

-- INDEX: crm_equipmentreservation_order_id_e9f68c20
CREATE INDEX "crm_equipmentreservation_order_id_e9f68c20" ON "crm_equipmentreservation" ("order_id");

-- INDEX: crm_ingredientreservation_ingredient_id_a8564254
CREATE INDEX "crm_ingredientreservation_ingredient_id_a8564254" ON "crm_ingredientreservation" ("ingredient_id");

-- INDEX: crm_ingredientreservation_order_id_17138f75
CREATE INDEX "crm_ingredientreservation_order_id_17138f75" ON "crm_ingredientreservation" ("order_id");

-- INDEX: crm_interaction_client_id_e63a8170
CREATE INDEX "crm_interaction_client_id_e63a8170" ON "crm_interaction" ("client_id");

-- INDEX: crm_interaction_manager_id_24afb2b9
CREATE INDEX "crm_interaction_manager_id_24afb2b9" ON "crm_interaction" ("manager_id");

-- INDEX: crm_order_client_id_8ed70023
CREATE INDEX "crm_order_client_id_8ed70023" ON "crm_order" ("client_id");

-- INDEX: crm_order_manager_id_039a402f
CREATE INDEX "crm_order_manager_id_039a402f" ON "crm_order" ("manager_id");

-- INDEX: crm_orderitem_custom_tech_card_id_5e4ea50e
CREATE INDEX "crm_orderitem_custom_tech_card_id_5e4ea50e" ON "crm_orderitem" ("custom_tech_card_id");

-- INDEX: crm_orderitem_dish_id_e3114b2a
CREATE INDEX "crm_orderitem_dish_id_e3114b2a" ON "crm_orderitem" ("dish_id");

-- INDEX: crm_orderitem_ingredient_id_2185a1eb
CREATE INDEX "crm_orderitem_ingredient_id_2185a1eb" ON "crm_orderitem" ("ingredient_id");

-- INDEX: crm_orderitem_order_id_7ec9f773
CREATE INDEX "crm_orderitem_order_id_7ec9f773" ON "crm_orderitem" ("order_id");

-- INDEX: crm_pickingsession_picker_id_ee342393
CREATE INDEX "crm_pickingsession_picker_id_ee342393" ON "crm_pickingsession" ("picker_id");

-- INDEX: crm_productionreservation_order_id_4efb72f7
CREATE INDEX "crm_productionreservation_order_id_4efb72f7" ON "crm_productionreservation" ("order_id");

-- INDEX: crm_route_logistician_id_a5ae8d10
CREATE INDEX "crm_route_logistician_id_a5ae8d10" ON "crm_route" ("logistician_id");

-- INDEX: crm_routestop_delivery_id_c0c90c7b
CREATE INDEX "crm_routestop_delivery_id_c0c90c7b" ON "crm_routestop" ("delivery_id");

-- INDEX: crm_routestop_proof_reviewed_by_id_27311351
CREATE INDEX "crm_routestop_proof_reviewed_by_id_27311351" ON "crm_routestop" ("proof_reviewed_by_id");

-- INDEX: crm_routestop_proof_uploaded_by_id_13f26b97
CREATE INDEX "crm_routestop_proof_uploaded_by_id_13f26b97" ON "crm_routestop" ("proof_uploaded_by_id");

-- INDEX: crm_routestop_route_id_38bf345b
CREATE INDEX "crm_routestop_route_id_38bf345b" ON "crm_routestop" ("route_id");

-- INDEX: crm_techcard_approved_by_id_32ef922d
CREATE INDEX "crm_techcard_approved_by_id_32ef922d" ON "crm_techcard" ("approved_by_id");

-- INDEX: crm_techcard_dish_id_277af818
CREATE INDEX "crm_techcard_dish_id_277af818" ON "crm_techcard" ("dish_id");

-- INDEX: crm_techcard_dish_id_version_label_b05cfe34_uniq
CREATE UNIQUE INDEX "crm_techcard_dish_id_version_label_b05cfe34_uniq" ON "crm_techcard" ("dish_id", "version_label");

-- INDEX: crm_techcardcomponent_ingredient_id_4ce9ea00
CREATE INDEX "crm_techcardcomponent_ingredient_id_4ce9ea00" ON "crm_techcardcomponent" ("ingredient_id");

-- INDEX: crm_techcardcomponent_tech_card_id_623c4128
CREATE INDEX "crm_techcardcomponent_tech_card_id_623c4128" ON "crm_techcardcomponent" ("tech_card_id");

-- INDEX: crm_techcardvariant_tech_card_id_43f7c6d6
CREATE INDEX "crm_techcardvariant_tech_card_id_43f7c6d6" ON "crm_techcardvariant" ("tech_card_id");

-- INDEX: crm_user_groups_group_id_93d3047c
CREATE INDEX "crm_user_groups_group_id_93d3047c" ON "crm_user_groups" ("group_id");

-- INDEX: crm_user_groups_user_id_5847c7a0
CREATE INDEX "crm_user_groups_user_id_5847c7a0" ON "crm_user_groups" ("user_id");

-- INDEX: crm_user_groups_user_id_group_id_56d4cc88_uniq
CREATE UNIQUE INDEX "crm_user_groups_user_id_group_id_56d4cc88_uniq" ON "crm_user_groups" ("user_id", "group_id");

-- INDEX: crm_user_user_permissions_permission_id_0f701f96
CREATE INDEX "crm_user_user_permissions_permission_id_0f701f96" ON "crm_user_user_permissions" ("permission_id");

-- INDEX: crm_user_user_permissions_user_id_047208b5
CREATE INDEX "crm_user_user_permissions_user_id_047208b5" ON "crm_user_user_permissions" ("user_id");

-- INDEX: crm_user_user_permissions_user_id_permission_id_72b1e4e1_uniq
CREATE UNIQUE INDEX "crm_user_user_permissions_user_id_permission_id_72b1e4e1_uniq" ON "crm_user_user_permissions" ("user_id", "permission_id");

-- INDEX: crm_userrole_role_id_764fcdba
CREATE INDEX "crm_userrole_role_id_764fcdba" ON "crm_userrole" ("role_id");

-- INDEX: crm_userrole_user_id_e281baa8
CREATE INDEX "crm_userrole_user_id_e281baa8" ON "crm_userrole" ("user_id");

-- INDEX: crm_userrole_user_id_role_id_fa7b18da_uniq
CREATE UNIQUE INDEX "crm_userrole_user_id_role_id_fa7b18da_uniq" ON "crm_userrole" ("user_id", "role_id");

-- INDEX: reports_report_created_by_id_e9adac24
CREATE INDEX "reports_report_created_by_id_e9adac24" ON "reports_report" ("created_by_id");
