"""A list of all Snowflake SQL key words.

https://docs.snowflake.com/en/sql-reference/reserved-keywords.html
"""

snowflake_reserved_keywords = """ALL
ALTER
AND
ANY
AS
ASOF
BETWEEN
BY
CAST
CHECK
CONNECT
CONNECTION
CONSTRAINT
CREATE
CURRENT
CURRENT_DATE
CURRENT_TIME
CURRENT_TIMESTAMP
CURRENT_USER
DELETE
DECLARE
DISTINCT
DROP
ELSE
EXISTS
FOLLOWING
FOR
FROM
FULL
GRANT
GROUP
GSCLUSTER
HAVING
ILIKE
IN
INCREMENT
INNER
INSERT
INSERT_ONLY
INTERSECT
INTO
IS
JOIN
LATERAL
LEFT
LIKE
LOCALTIME
LOCALTIMESTAMP
MATCH_CONDITION
MATCH_RECOGNIZE
MINUS
NATURAL
NOT
NULL
NULL_IF
OF
ON
OR
ORDER
QUALIFY
REGEXP
REVOKE
RIGHT
RLIKE
ROW
ROWS
SAMPLE
SELECT
SET
SOME
START
STRICT
TABLE
TABLESAMPLE
THEN
TO
TRIGGER
TRY_CAST
UNION
UNIQUE
UNPIVOT
UPDATE
USING
VALUES
WHEN
WHENEVER
WHERE
WITH
"""

snowflake_unreserved_keywords = """
ABORT
ABORT_STATEMENT
ACCESS
ACCOUNT
ACCOUNTS
ADD
ADMIN
AFTER
AGGREGATE
ALLOW_DUPLICATE
ALLOW_OVERLAPPING_EXECUTION
ALLOW_WRITES
ALLOWED_IP_LIST
ALLOWED_NETWORK_RULE_LIST
ALLOWED_VALUES
ALWAYS
API
API_INTEGRATION
APPEND_ONLY
APPLY
ARRAY
ASC
AT
ATTACH
AUTHORIZATION
AUTHORIZATIONS
AUTO
AUTO_COMPRESS
AUTO_INCREMENT
AUTO_INGEST
AUTO_REFRESH
AUTO_RESUME
AUTO_SUSPEND
AUTOINCREMENT
AVRO
AWS_KEY_ID
AWS_ROLE
AWS_SECRET_KEY
AWS_SNS
AWS_SNS_ROLE_ARN
AWS_SNS_TOPIC
AWS_SNS_TOPIC_ARN
AWS_TOKEN
AZURE
AZURE_EVENT_GRID
AZURE_EVENT_GRID_TOPIC_ENDPOINT
AZURE_SAS_TOKEN
AZURE_STORAGE_QUEUE
AZURE_STORAGE_QUEUE_PRIMARY_URI
AZURE_TENANT_ID
BASE64
BEFORE
BEGIN
BERNOULLI
BINARY
BINARY_AS_TEXT
BINARY_FORMAT
BINDING
BLOCK
BLOCKED_IP_LIST
BLOCKED_NETWORK_RULE_LIST
BODY
BROTLI
BZ2
CACHE
CALL
CALLED
CALLER
CASCADE
CASE
CASE_INSENSITIVE
CASE_SENSITIVE
CASES
CHAIN
CHANGE_TRACKING
CHANGES
CHARACTER
CLONE
CLUSTER
CLUSTERING
COLLATE
COLUMN
COLUMNS
COMMENT
COMMIT
COMPRESSION
CONCURRENTLY
CONNECT_BY_ROOT
CONTEXT_HEADERS
CONTINUE
COPY
COPY_OPTIONS
CREDENTIALS
CREDIT_QUOTA
CROSS
CSV
CUBE
CURRENT_ACCOUNT
CURRENT_CLIENT
CURRENT_DATABASE
CURRENT_IP_ADDRESS
CURRENT_REGION
CURRENT_ROLE
CURRENT_SCHEMA
CURRENT_SCHEMAS
CURRENT_SESSION
CURRENT_STATEMENT
CURRENT_TRANSACTION
CURRENT_VERSION
CURRENT_WAREHOUSE
CURSOR
CYCLE
DAILY
DATA
DATA_FORMAT
DATA_RETENTION_TIME_IN_DAYS
DATABASE
DATABASES
DATE
DATE_FORMAT
DAYS_TO_EXPIRY
DEBUG
DEFAULT
DEFAULT_DDL_COLLATION
DEFAULT_NAMESPACE
DEFAULT_ROLE
DEFAULT_SECONDARY_ROLES
DEFAULT_WAREHOUSE
DEFERRABLE
DEFERRED
DEFINE
DEFLATE
DELEGATED
DESC
DESCRIBE
DETAILED_OUTPUT
DIRECTION
DIRECTORY
DISABLE
DISABLE_AUTO_CONVERT
DISABLE_SNOWFLAKE_DATA
DISABLED
DISPLAY_NAME
DO
DOMAIN
DOUBLE
DOWNSTREAM
DYNAMIC
ECONOMY
EMAIL
EMPTY
EMPTY_FIELD_AS_NULL
ENABLE
ENABLE_OCTAL
ENABLED
ENCODING
ENCRYPTION
END
END_TIMESTAMP
ENFORCE_LENGTH
ENFORCED
ENUM
ERROR
ERROR_INTEGRATION
ERROR_ON_COLUMN_COUNT_MISMATCH
ESCAPE
ESCAPE_UNENCLOSED_FIELD
EVENT
EXCEPT
EXCEPTION
EXCHANGE
EXCLUDE
EXECUTE
EXECUTION
EXPLAIN
EXTENSION
EXTERNAL
EXTERNAL_ACCESS_INTEGRATIONS
EXTERNAL_STAGE
FATAL
FETCH
FIELD_DELIMITER
FIELD_OPTIONALITY_ENCLOSED_BY
FIELD_OPTIONALLY_ENCLOSED_BY
FILE
FILE_EXTENSION
FILE_FORMAT
FILES
FILTER
FINAL
FIRST
FIRST_NAME
FOR
FORCE
FOREIGN
FORMAT
FORMAT_NAME
FORMATS
FREQUENCY
FUNCTION
FUNCTIONS
FUTURE
GCP_PUBSUB
GCP_PUBSUB_SUBSCRIPTION_NAME
GCP_PUBSUB_TOPIC_NAME
GCS
GET
GLOBAL
GRANTED
GRANTS
GROUPING
GZIP
HANDLER
HEADER
HEADERS
HEX
HISTORY
IDENTIFIER
IDENTITY
IF
IGNORE
IGNORE_UTF8_ERRORS
IMMEDIATE
IMMEDIATELY
IMMUTABLE
IMPORT
IMPORTED
IMPORTS
INCLUDE
INCLUDE_QUERY_ID
INDEX
INFO
INFORMATION
INITIALIZE
INITIALLY
INITIALLY_SUSPENDED
INPUT
INTEGRATION
INTEGRATIONS
INTERVAL
ISSUE
JAVA
JAVASCRIPT
JSON
KEY
KMS_KEY_ID
LANGUAGE
LARGE
LAST
LAST_NAME
LAST_QUERY_ID
LAST_TRANSACTION
LET
LIMIT
LIST
LISTING
LOCAL
LOCATION
LOCKS
LOG_LEVEL
LOGIN_NAME
LS
LZO
M
MAIN_FILE
MANAGE
MANAGED
MASKING
MASTER_KEY
MATCH
MATCH_BY_COLUMN_NAME
MATCHED
MATCHES
MATERIALIZED
MAX_BATCH_ROWS
MAX_CLUSTER_COUNT
MAX_CONCURRENCY_LEVEL
MAX_DATA_EXTENSION_TIME_IN_DAYS
MAX_FILE_SIZE
MAX_SIZE
MAXVALUE
MEASURES
MERGE
MIDDLE_NAME
MIN_CLUSTER_COUNT
MINS_TO_BYPASS_MFA
MINS_TO_UNLOCK
MINVALUE
ML
MODEL
MODIFIED_AFTER
MODIFY
MONITOR
MONTHLY
MUST_CHANGE_PASSWORD
NAME
NAN
NETWORK
NEVER
NEXT
NEXTVAL
NO
NOCACHE
NOCYCLE
NONE
NOORDER
NOTIFICATION
NOTIFICATION_INTEGRATION
NOTIFICATION_PROVIDER
NOTIFY
NOTIFY_USERS
NULL_IF
NULLS
OBJECT
OBJECTS
OFF
OFFSET
OMIT
ON_ERROR
ON_EVENT
ONE
ONLY
OPERATE
OPTIMIZATION
OPTION
OPTIONS
ORC
ORGANIZATION
OUTBOUND
OUTER
OVER
OVERLAPS
OVERRIDE
OVERWRITE
OWNER
OWNERSHIP
PACKAGES
PARALLEL
PARAMETERS
PARQUET
PARSE_HEADER
PARTITION
PASSWORD
PAST
PATTERN
PER
PERCENT
PERMUTE
PIPE
PIPE_EXECUTION_PAUSED
PIPES
PIVOT
POLICIES
POLICY
PRECEDING
PRECISION
PREFIX
PRESERVE_SPACE
PRIMARY
PRIOR
PRIVILEGES
PROCEDURE
PROCEDURES
PUBLIC
PURGE
PUT
PYTHON
QUERIES
QUERY_WAREHOUSE
QUEUE
RANGE
RAW_DEFLATE
READ
RECLUSTER
RECORD_DELIMITER
RECURSIVE
REFERENCE_USAGE
REFERENCES
REFRESH
REFRESH_MODE
REFRESH_ON_CREATE
REGIONS
REMOVE
RENAME
REPEATABLE
REPLACE
REPLACE_INVALID_CHARACTERS
REPLICATION
REQUEST_TRANSLATOR
RESET
RESOURCE
RESOURCE_MONITOR
RESPECT
RESPONSE_TRANSLATOR
RESTRICT
RESTRICTIONS
RESULT
RESULTSET
RESUME
RETURN
RETURN_ALL_ERRORS
RETURN_ERRORS
RETURN_FAILED_ONLY
RETURNS
RM
ROLE
ROLES
ROLLBACK
ROLLUP
ROOT_LOCATION
ROUTINE
ROUTINES
ROW
RSA_PUBLIC_KEY
RSA_PUBLIC_KEY_2
RUNNING
RUNTIME_VERSION
S3
SCALA
SCALING_POLICY
SCHEDULE
SCHEMA
SCHEMAS
SEARCH
SECONDARY
SECRETS
SECURE
SECURITY
SEED
SEPARATOR
SEQUENCE
SEQUENCES
SERVER
SESSION
SESSION_USER
SETS
SHARE
SHARE_RESTRICTIONS
SHARES
SHOW
SHOW_INITIAL_ROWS
SINGLE
SIZE_LIMIT
SKIP
SKIP_BLANK_LINES
SKIP_BYTE_ORDER_MARK
SKIP_FILE
SKIP_HEADER
SNAPPY
SNAPPY_COMPRESSION
SNOWFLAKE_FULL
SNOWFLAKE_SSE
SOURCE_COMPRESSION
SQL
STAGE
STAGE_COPY_OPTIONS
STAGE_FILE_FORMAT
STAGES
STANDARD
START_TIMESTAMP
STARTS
STATEMENT
STATEMENT_QUEUED_TIMEOUT_IN_SECONDS
STATEMENT_TIMEOUT_IN_SECONDS
STORAGE
STORAGE_ALLOWED_LOCATIONS
STORAGE_AWS_EXTERNAL_ID
STORAGE_AWS_OBJECT_ACL
STORAGE_AWS_ROLE_ARN
STORAGE_BASE_URL
STORAGE_BLOCKED_LOCATIONS
STORAGE_INTEGRATION
STORAGE_LOCATION
STORAGE_LOCATIONS
STORAGE_PROVIDER
STREAM
STREAMLIT
STREAMLITS
STREAMS
STRIP_NULL_VALUES
STRIP_OUTER_ARRAY
STRIP_OUTER_ELEMENT
SUBPATH
SUPPORT
SUSPEND
SUSPEND_IMMEDIATE
SUSPENDED
SWAP
SYSDATE
SYSTEM
TABLES
TABLESPACE
TABULAR
TAG
TARGET_LAG
TARGET_PATH
TASK
TASKS
TEMP
TEMPLATE
TEMPORARY
TERSE
TEXT
TIME
TIME_FORMAT
TIMESTAMP
TIMESTAMP_FORMAT
TOP
TRACE
TRACE_LEVEL
TRANSACTION
TRANSACTIONS
TRANSIENT
TRIGGERS
TRIM_SPACE
TRUNCATE
TRUNCATECOLUMNS
TYPE
UNBOUNDED
UNDROP
UNMATCHED
UNSET
UNSIGNED
URL
US
USAGE
USE
USE_ANY_ROLE
USER
USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE
USER_TASK_TIMEOUT_MS
USERS
UTF8
VALIDATE_UTF8
VALIDATION_MODE
VALUE
VARIABLES
VARIANT
VARYING
VERSION
VIEW
VIEWS
VOLATILE
VOLUME
VOLUMES
WAIT_FOR_COMPLETION
WAREHOUSE
WAREHOUSE_SIZE
WAREHOUSE_TYPE
WAREHOUSES
WARN
WEEKLY
WINDOW
WITH
WITHIN
WITHOUT
WORK
WOY
WRAPPER
WRITE
XML
YEARLY
ZONE
ZSTD
"""
