-- The following script generates mysql tables to achieve three tasks:

-- 1. A table to record requests and success and failure requests to the smart home server.
-- 3. A table to record resources occupied and available in the smart home.

CREATE DATABASE Smarthomes;
USE Smarthomes;

CREATE TABLE API_Request
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  User            VARCHAR(150) NOT NULL,                # User requesting the task
  Task            VARCHAR(150) NOT NULL,                # Task being requested
  Timestamp        TIMESTAMP,                      # Time of request
  Validity          INT,                                 # Time of validity of the task.
  Status           VARCHAR(150) NOT NULL,    # Status of request.
  ip_address  INT(4) UNSIGNED NOT NULL, #IP address of the request
  Message             TEXT,                                         # Message for the request.
  Resources_allowed      TEXT,                               #Resources granted to the user. 
  PRIMARY KEY     (id)                                  # Make the id the primary key
);

CREATE TABLE Resource_ownership
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  Owner            VARCHAR(150) NOT NULL,                # User having the resource.
  Task            VARCHAR(150) NOT NULL,                # Task belonging for the resource.
  Device        VARCHAR(150) NOT NULL,    #Device of the resource.
  Privilege     TEXT,                                        #Privilege/Resource of the device.
  Timestamp        TIMESTAMP,                      # Time of request
  Status           VARCHAR(150) NOT NULL,    # Status of request.
  PRIMARY KEY     (id)                                  # Make the id the primary key
);
