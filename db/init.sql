-- CREATE DATABASE BDAT_FE_simulations;
-- use BDAT_FE_simulations;

-- CREATE TABLE timesimtransisomat_first_step01
-- (
--    id int NOT NULL identity(1001, 1) primary key,
--     n_transmitter int NOT NULL,
--     n_receiver int NOT NULL,
--     distance float DEFAULT NULL,
--     plate_thickness int NOT NULL,
--     porosity decimal(10,0) NOT NULL,
--     result_step_01 text,
--     p_status VARCHAR,
--     time_s time DEFAULT NULL,
--     image_s blob
-- );


-- INSERT INTO timesimtransisomat_first_step01
--   (id, n_transmitter, n_receiver, distance, plate_thickness, porosity, result_step_01, p_status, time_s, image_s)
-- VALUES
--   ('1', '1','5','0.2','5','5', '', 'Not Started', '', '');
-- CREATE TABLE testtable (
--   name VARCHAR(20),
--   color VARCHAR(10)
-- );

-- INSERT INTO test_table
--   (name, color)
-- VALUES
--   ('dev', 'blue'),
--   ('pro', 'yellow');

-- CREATE DATABASE knights;
-- use knights;

-- Prueba para ver el problema con docker y la base de datos

CREATE TABLE favorite_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');
-- INSERT INTO timesimtransisomat_first_step01 
--   (n_transmitter, n_receiver, distance, plate_thickness, porosity, p_status) 
-- VALUES
--   (9, 9, 9, 9, 9, 9);
