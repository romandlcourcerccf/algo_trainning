select cal_date as days,  sum(price_per_item * cnt) as sku  from transactions_another_one
group by days