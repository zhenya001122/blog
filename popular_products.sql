SELECT "shop_product"."id",
       "shop_product"."title",
       "shop_product"."color",
       "shop_product"."image",
       "shop_product"."cost",
       "shop_product"."cost_byn",
       "shop_product"."status",
       "shop_product"."external_id",
       "shop_product"."link",
       SUM(("shop_product"."cost" * "shop_purchase"."count")) AS "sold"
FROM "shop_product"
LEFT OUTER JOIN "shop_purchase" ON ("shop_product"."id" = "shop_purchase"."product_id")
GROUP BY "shop_product"."id"