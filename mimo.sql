PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE DAY_TASK
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
TASK_NAME TEXT,
DETAIL TEXT,
STAR INTEGER,
COMMENT TEXT,
TIME TEXT
);
COMMIT;
