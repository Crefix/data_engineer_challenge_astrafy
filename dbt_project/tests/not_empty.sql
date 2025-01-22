SELECT *
FROM {{ model }}
WHERE {{ column_name }} IS NULL
   OR {{ column_name }} = ''