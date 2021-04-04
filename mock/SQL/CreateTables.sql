CREATE TABLE IF NOT EXISTS User_ (
	UserId integer PRIMARY KEY AUTOINCREMENT,
	Name text,
	GroupNameOveride text
);





CREATE TABLE IF NOT EXISTS Group_ (
	GroupId integer PRIMARY KEY AUTOINCREMENT,
	Name text,
	Description text,
	Icon text,
	User integer,
	FOREIGN KEY (User)
		REFERENCES User_ (UserId) 
                ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS  Client_ (
	ClientId integer PRIMARY KEY AUTOINCREMENT,
	Name text,
	Description text,
	Icon text,
	
	Group_ integer,
	FilePath text,
	FOREIGN KEY (Group_)
		REFERENCES Group_ (GroupId)
                ON UPDATE CASCADE
                ON DELETE CASCADE 

);

CREATE TABLE IF NOT EXISTS Project_ (
	ProjectId integer PRIMARY KEY AUTOINCREMENT,
	Name text,
	Description text,
	Icon text,
	ProjectType text,
	Client integer,
	Delivery blob,
	Status integer,
	FilePath text,
	FOREIGN KEY (Client)
		REFERENCES Client_ (ClientId) 
                ON UPDATE CASCADE
                ON DELETE CASCADE 
);

