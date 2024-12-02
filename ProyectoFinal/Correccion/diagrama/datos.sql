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