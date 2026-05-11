CREATE TABLE ADVISOR (
    advisor_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    credentials VARCHAR(50),
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20)
);

CREATE TABLE CLIENT (
    client_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL,
    advisor_id INT,

    CONSTRAINT fk_client_advisor
        FOREIGN KEY (advisor_id)
        REFERENCES ADVISOR(advisor_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE ACCOUNT (
    account_id INT PRIMARY KEY,
    client_id INT NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    currency CHAR(3) NOT NULL DEFAULT 'USD',
    open_date DATE NOT NULL,

    CONSTRAINT fk_account_client
        FOREIGN KEY (client_id)
        REFERENCES CLIENT(client_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT chk_account_balance
        CHECK (balance >= 0)
);

CREATE TABLE `TRANSACTION` (
    transaction_id INT PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    description VARCHAR(255),

    CONSTRAINT fk_transaction_account
        FOREIGN KEY (account_id)
        REFERENCES ACCOUNT(account_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT chk_transaction_amount
        CHECK (amount > 0)
);

CREATE TABLE APPOINTMENT (
    appointment_id INT PRIMARY KEY,
    client_id INT NOT NULL,
    advisor_id INT NOT NULL,
    appt_date DATE NOT NULL,
    appt_time TIME NOT NULL,
    notes VARCHAR(255),

    CONSTRAINT fk_appointment_client
        FOREIGN KEY (client_id)
        REFERENCES CLIENT(client_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_appointment_advisor
        FOREIGN KEY (advisor_id)
        REFERENCES ADVISOR(advisor_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE COMPLIANCE_RECORD (
    compliance_id INT PRIMARY KEY,
    review_date DATE NOT NULL,
    review_type VARCHAR(100) NOT NULL,
    outcome VARCHAR(100) NOT NULL,
    reviewed_by VARCHAR(100) NOT NULL
);

CREATE TABLE EMPLOYEE (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(75) NOT NULL,
    employment_type VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20)
);