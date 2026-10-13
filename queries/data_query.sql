SELECT 
    s.SalesOrderNumber,
    s.SalesOrderLineNumber,
    s.OrderDate,
    pc.EnglishProductCategoryName AS Category,
    ps.EnglishProductSubcategoryName AS Subcategory,
    p.ProductLine,
    p.ModelName AS Model,
    p.EnglishProductName AS Product,
    p.Color,
    s.OrderQuantity,
    s.UnitPrice,
    s.ExtendedAmount,
    s.SalesAmount
FROM FactInternetSales s
JOIN DimProduct p 
    ON s.ProductKey = p.ProductKey
JOIN DimProductSubcategory ps 
    ON p.ProductSubcategoryKey = ps.ProductSubcategoryKey
JOIN DimProductCategory pc 
    ON ps.ProductCategoryKey = pc.ProductCategoryKey
ORDER BY 
    s.OrderDate DESC;