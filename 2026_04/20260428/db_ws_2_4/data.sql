CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  user_id INT,
  amount TEXT,
  transaction_date DATE,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO transactions (user_id, amount, transaction_date)
VALUES
(1, 500, '2024-03-15'),
(2, 700, '2024-03-16'),
(3, 200, '2024-03-17'),
(4, 1000, '2024-03-18');



SELECT first_name, last_name, transactions.amount, transactions.transaction_date
FROM users
INNER JOIN transactions
ON users.id = transactions.user_id;


SELECT first_name, last_name, sum(amount) AS total_amount
FROM users
INNER JOIN transactions
ON users.id = transactions.user_id
GROUP BY transactions.user_id;