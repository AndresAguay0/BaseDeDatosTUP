SELECT 
    o.id_orden, 
    c.nombre AS cliente, 
    p.nombre AS producto, 
    d.cantidad, 
    d.precio_unitario
FROM Ordenes o
INNER JOIN DetalleOrden d ON o.id_orden = d.id_orden
INNER JOIN Productos p ON d.id_producto = p.id_producto
INNER JOIN Clientes c ON o.id_cliente = c.id_cliente
ORDER BY o.fecha DESC;

SELECT * FROM Productos WHERE stock < 10;


SELECT 
    c.nombre AS cliente, 
    COUNT(o.id_orden) AS total_ordenes
FROM Clientes c
INNER JOIN Ordenes o ON c.id_cliente = o.id_cliente
GROUP BY c.id_cliente
ORDER BY total_ordenes DESC;