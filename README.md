# Database Manager-NBA

A Database to help individuals manage NBA players for Fantasy Basketball.

Snapshot images provided at the end of the Readme, showing the output.
<br/>
<br/>
*Currently under maintenance and needs new hosting platform. However, all the files in this repository will remain unchanged.*
<br/>
Re-uploaded to replace an older repository: https://github.com/pgill20/Database-Manager

## Database Outline:
### Teams
This is any of the given NBA teams, each with 13 player slots that have to be filled to be considered to play for that year. Teams do not have mandatory player positions, a team could be made of all “C” positions.

<div align="center">

| Name | Value |
| :---: | :---: |
| team_id:          | int, auto_inc, not NULL, PK, unique | 
| team_name:        | varchar, not NULL                   |
| total_fines:      | int, not NULL                       |
| salary_available: | int, not NULL                       |
| best_player:      | varchar, not NULL                   |

</div>

Relationship: A 1:M relationship between Players and Teams with Teams (team_id) as a FK within Players and a 1:1 relationship between Teams and Head_Coaches with team (team_id) as FK within Head_Coaches). A 1:1 relationship with Stadiums with team (team_id) as FK in Stadiums.

### Players

This is the entire player pool of the NBA. Players on teams are active and players not currently on a team are not active.  Must have team field if active. 

<div align="center">
  
| Name | Value |
| :---: | :---: |
player_id:                            	| int, auto_inc, not NULL, PK, unique
first_name:                            	| varchar, not NULL
last_name:                            	| varchar, not NULL
speciality:			| varchar, not NULL
team:                               	| int, FK, not NULL if Active
salary:                               	| int, not NULL 
height:                                   	| int, not NULL (cm)
weight:                                  	| int, not NULL (lbs)
birthday:                                	| date
primary_position:                | varchar, could be “PG”, “SG”, “SF”, “PF”, “C”, not NULL
secondary_position:        	| varchar, could be “PG”, “SG”, “SF”, “PF”, “C”
fg:                                     	| decimal, not NULL, float, field goal percentage 
ft:                                  	| decimal, not NULL, free throw percentage 
ppg:                                   	| float, points per game 
rpg:                                   	| decimal, not NULL, rebounds per game 
apg:                                  	| decimal, not NULL, assists per game 
spg:                                      	| decimal, not NULL, steals per game 
bpg:                                   	| decimal, not NULL, blocks per game 
tpg:                                 	| decimal, not NULL, turnovers per game 

</div>

Relationship:                          A 1:M relationship between Players and Teams with Teams (team_id) as a FK inside of Players and a M:M relationship between Players and Trainers shown with the player_trainer entity.

### Head_Coaches

Each of the NBA teams have one Head_Coaches. Each head_coach has a first_name and a last_name, along with the team they are part of currently.

<div align="center">
  
| Name | Value |
| :---: | :---: |
coach_id:                            	| int, auto_inc, not NULL, PK, unique
first_name:                    	| varchar, not NULL
last_name:                    	| varchar, not NULL
team:                               	| varchar, not NULL

</div>

Relationship:                          A 1:1 relationship between Head_Coaches and Teams with team (team_id) as FK within Head_Coaches.

### Trainers

A trainer can be approached by any of the NBA players when they want to work on any of their skill sets or want to develop new skills. Each trainer has a first_name and last_name, along with their speciality of skill(s) they can teach any of the NBA players.

<div align="center">
  
| Name | Value |
| :---: | :---: |
trainer_id:                           	| int, auto_inc, not NULL, PK, unique
first_name:                    	| varchar, not NULL
last_name:                    	| varchar, not NULL
specialty:                         	| varchar, not NULL

</div>

Relationship:                    	A M:M relationship between Players and Trainers shown with the Players_Trainers entity.

### Stadiums

The homecourt for each Team where the players (Player) come to play. Each stadium has a name and their respective team.

<div align="center">
  
| Name | Value |
| :---: | :---: |
stadium_id:                         	| int, auto_inc, not NULL, PK, unique
stadium_name:		| varchar, not NULL
city:				| varchar, not NULL
team:				| varchar, not NULL
state:				| varchar, not NULL

</div>

Relationship:                         	A 1:1 relationship between Stadiums and Teams with team (team_id) as FK inside of Stadiums.

## Intersection Table:

### Players_Trainers

Relationship between Players and Trainers.

<div align="center">
  
| Name | Value |
| :---: | :---: |
player_rel_id:			| int, not NULL, PK, FK
player_last_name: 		| varchar, not NULL, PK, FK
trainer_rel_id: 			| int, not NULL, PK, FK
player_last_name: 		| varchar, not NULL, PK, FK

</div>

Relationship: 			A M:M relationship for Players and Player_Trainers with player_id and trainer_id as keys.

## Basketball Manager Entity-Relationship (ER) Diagram:

<img width="1000" alt="11" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/97425e3b-7c95-4bb4-b69b-6d6131f68a61">

## Basketball Manager Schema:

<img width="1000" alt="12" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/302988bf-6aa9-4079-82ed-13b39a6772a3">

## The following are snapshots of the functioning Data Manager website:

<div align="center">

<img width="1000" alt="13" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/752e7ad0-3f08-4754-b074-72d25efa4d88">
<img width="1000" alt="14" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/ca65d1ea-2883-4c68-8373-4c4efa6c2dec">
<img width="1000" alt="15" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/a5e90572-e484-44e2-9135-5cb19d255150">
<img width="1000" alt="16" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/d3afc207-3a2a-4543-b3d7-3f8aaa40924f">
<img width="1000" alt="17" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/32e97601-d3af-471b-ba55-97101799ce4c">
<img width="1000" alt="18" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/4788593a-8c20-47c5-a6fb-207f6612c91a">
<img width="1000" alt="19" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/7df198b0-64fc-4f7f-bde1-43e7d34f6880">
<img width="1000" alt="20" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/ceb826a2-2b75-4009-84a3-5f3ca22a2c81">
<img width="1000" alt="21" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/a4e09dd8-20c6-4b83-a563-0adc9811eb48">
<img width="1000" alt="22" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/a0d79754-d3b0-4aab-8385-731170a8e22b">
<img width="1000" alt="23" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/716ce428-da07-485c-8881-1949c53a1ca2">
<img width="1000" alt="24" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/0b3b7ce3-46b9-486d-8888-414f478bd25c">
<img width="1000" alt="25" src="https://github.com/pgill20/Database-Manager-NBA/assets/72182630/a18fd286-28cb-48c2-aa20-6f189066b667">

</div>
