instructions = [
    'SET FOREIGN_KEY_CHECKS = 0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS = 1;',
    """
        CREATE TABLE user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
    """,
    """
        CREATE TABLE todo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL, 
            FOREIGN KEY (created_by) REFERENCES user(id)
        );
    """
]