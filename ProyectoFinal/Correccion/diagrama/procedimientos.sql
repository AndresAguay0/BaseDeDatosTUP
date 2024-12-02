DELIMITER $$

CREATE PROCEDURE RegistrarOrden (
    IN cliente_id INT, 
    IN producto_id INT, 
    IN cantidad INT
)
BEGIN
    DECLARE precio DECIMAL(10, 2);

    SELECT precio INTO precio FROM Productos WHERE id_producto = producto_id;

    INSERT INTO Ordenes (id_cliente, fecha) VALUES (cliente_id, NOW());
    SET @orden_id = LAST_INSERT_ID();

    INSERT INTO DetalleOrden (id_orden, id_producto, cantidad, precio_unitario)
    VALUES (@orden_id, producto_id, cantidad, precio);
END $$

DELIMITER ;