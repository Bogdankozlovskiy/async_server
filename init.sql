create table post (
	id serial,
	title varchar(255) not null,
	body text
);
insert into post(title, body) values('first post', 'это приведственный пост')