-- Tables created on steve's machine for importing data
-- 

CREATE TABLE clthackathon_sca.tweets (
   tweet_id BIGINT NOT NULL,
   tweet VARCHAR(200) NOT NULL,
   user_id BIGINT NOT NULL,
   user_text VARCHAR(15) NOT NULL,
   sentiment_score INT NOT NULL,
   sentiment_count INT NOT NULL,
   city VARCHAR(100),
   city_score DOUBLE,
   city_count INT,
  PRIMARY KEY (tweet_id)
) ENGINE = InnoDB ROW_FORMAT = DEFAULT;

CREATE TABLE clthackathon_sca.words (
   word VARCHAR(100) NOT NULL,
   twitter_id BIGINT NOT NULL,
   score FLOAT NOT NULL,
   count INT NOT NULL
) ENGINE = InnoDB ROW_FORMAT = DEFAULT;
