-- PostGre Queries for harris Teeter Data
-- 5-2-2013
-- Bill Schoonmaker

-- updates to remove extra spaces in description column after load
update "HarrisTeeterData"."customer-data"
set description = 'BEER'
where description = '  BEER';;
update "HarrisTeeterData"."customer-data"
set description = 'WINE'
where description = '  WINE';
update "HarrisTeeterData"."customer-data"
set description = 'DELI'
where description = '  DELI';
update "HarrisTeeterData"."customer-data"
set description = 'BAKERY'
where description = '  BAKERY';
update "HarrisTeeterData"."customer-data"
set description = 'BAKERY'
where description = ' BAKERY';

-- Show total sales grouped by description
SELECT 
  "customer-data".description,
  sum("customer-data".net_sales)
FROM 
  "HarrisTeeterData"."customer-data"
    group by   "customer-data".description
  order by sum("customer-data".net_sales) desc
  
  
  -- Show first day of sales 
  select min("customer-data".date) from "HarrisTeeterData"."customer-data";
  -- Show last day of sales
  select max("customer-data".date) from "HarrisTeeterData"."customer-data";
  
  -- Show sales transaction counts per day orderd by day
  select to_char("customer-data".date, 'YYYY Month DD Day'), count(*) from "HarrisTeeterData"."customer-data"
  group by to_char("customer-data".date, 'YYYY Month DD Day')
  order by count(*) desc
  
  -- Show total sales by household order by total sales descending
  SELECT 
  "customer-data".household_num, 
  sum("customer-data".net_sales)
FROM 
  "HarrisTeeterData"."customer-data"
  group by   "customer-data".household_num
  order by sum("customer-data".net_sales) desc


