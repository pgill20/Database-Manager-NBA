--get all attributes of teams to populate Teams table
SELECT * FROM Teams;

--remove team with the id
DELETE FROM Teams WHERE team_id = :team_id;

--add new team
INSERT INTO Teams(name, total_fines)
VALUES(:team_id, :name, :total_fines)

--get all attributes of players to populate Players table
SELECT * FROM Players;

--remove player
DELETE FROM Players WHERE player_id = :player_id;

--add NEW player
INSERT INTO Players(first_name, last_name, speciality, team, salary, height, weight, birthday, primary_positions, secondary_position, fg, ft, ppg, rpg, apg, spg, bpg, tpg)
VALUES(:player_id, :first_name, :last_name, :speciality, :team, :salary, :height, :weight, :birthday, :primary_positions, :secondary_position, :fg, :ft, :ppg, :rpg, :apg, :spg, :bpg, :tpg)

--get all attributes of head_coaches to populate Head_Coaches table
SELECT * FROM Head_Coaches;

--add NEW head_coach
INSERT INTO Head_coach(first_name, last_name, team)
VALUES(:coach_id, :first_name, :last_name, :team)

--remove head_coach
DELETE FROM Head_Coaches WHERE coach_id = :coach_id

--get all attributes of trainers to populate Trainers table
SELECT * FROM Trainers;

--add new trainer
INSERT INTO Trainers(first_name, last_name, specialty)
VALUES(:trainer_id, :first_name, :last_name, :specialty)

--remove trainer
DELETE FROM Trainers WHERE trainer_id = :trainre_id;

--get all attributes of stadiums to populate Stadiums table
SELECT * FROM Stadiums;

--add new stadium
INSERT INTO Stadiums(stadium_id, stadium_name, team, city, state)
VALUES(:stadium_id, :stadium_name, :team, :city, :state)

--remove stadium
DELETE FROM Stadiums WHERE stadium_id = :stadium_id;

--search for a Purchase Order
SELECT * FROM PurchaseOrder
Where orderID = :orderID;