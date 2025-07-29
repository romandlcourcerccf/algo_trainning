SELECT user_id,
       round(avg(prod_count), 2) as avg_order_size
FROM   (SELECT user_id,
               array_length(product_ids, 1) as prod_count
        FROM   (SELECT user_id,
                       order_id
                FROM   user_actions
                WHERE  order_id not in (SELECT order_id
                                        FROM   user_actions
                                        WHERE  action = 'cancel_order')) t
            LEFT JOIN orders using(order_id)
        GROUP BY user_id, product_ids
        ORDER BY user_id) as d
GROUP BY user_id limit 1000