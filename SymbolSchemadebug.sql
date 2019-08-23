create table prices_archiver_debug.Symbols (
  symbol varchar(255),
  name varchar(255),
  price float
);

create table prices_archiver_debug.StocksPrices (
  symbol varchar(255) not null,
  price float not null,
  date_added timestamp not null
);

create table prices_archiver_debug.StocksHistoricalPrices (
  symbol         varchar(255) not null,
  open           float        not null,
  high           float        not null,
  low            float        not null,
  change_percent float        not null,
  date           varchar(255)    not null
);