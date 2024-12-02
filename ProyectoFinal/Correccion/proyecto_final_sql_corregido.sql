CREATE TABLE Productos (
    id_producto INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(255),
    precio DECIMAL(10, 2) NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    direccion TEXT
);

CREATE TABLE Ordenes (
    id_orden INTEGER PRIMARY KEY AUTO_INCREMENT,
    fecha DATETIME NOT NULL,
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE DetalleOrden (
    id_detalle INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_orden INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

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

INSERT INTO Productos (nombre, categoria, precio, stock) VALUES
('Producto A', 'Categoría 1', 100.00, 50),
('Producto B', 'Categoría 2', 200.00, 30),
('Producto C', 'Categoría 1', 150.00, 20),
('Producto D', 'Categoría 3', 250.00, 10),
('Producto E', 'Categoría 2', 300.00, 25),
('Producto F', 'Categoría 1', 50.00, 100),
('Producto G', 'Categoría 3', 400.00, 5),
('Producto H', 'Categoría 2', 120.00, 60),
('Producto I', 'Categoría 1', 80.00, 40),
('Producto J', 'Categoría 3', 220.00, 15);


INSERT INTO Clientes (nombre, email, direccion) VALUES
('Cliente 1', 'cliente1@example.com', 'Dirección 1'),
('Cliente 2', 'cliente2@example.com', 'Dirección 2'),
('Cliente 3', 'cliente3@example.com', 'Dirección 3'),
('Cliente 4', 'cliente4@example.com', 'Dirección 4'),
('Cliente 5', 'cliente5@example.com', 'Dirección 5'),
('Cliente 6', 'cliente6@example.com', 'Dirección 6'),
('Cliente 7', 'cliente7@example.com', 'Dirección 7'),
('Cliente 8', 'cliente8@example.com', 'Dirección 8'),
('Cliente 9', 'cliente9@example.com', 'Dirección 9'),
('Cliente 10', 'cliente10@example.com', 'Dirección 10');


INSERT INTO Ordenes (fecha, id_cliente) VALUES
('2024-01-01', 1), ('2024-01-02', 1), ('2024-01-03', 1),
('2024-01-01', 2), ('2024-01-05', 2), ('2024-01-10', 2),
('2024-01-02', 3), ('2024-01-08', 3), ('2024-01-15', 3),
('2024-01-03', 4);

INSERT INTO DetalleOrden (id_orden, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 2, 100.00), (1, 2, 1, 200.00), (2, 3, 3, 150.00),
(3, 4, 1, 250.00), (4, 5, 2, 300.00), (5, 6, 4, 50.00);

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