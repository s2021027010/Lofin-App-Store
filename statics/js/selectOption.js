// Map your choices to your option value
var lookup = {
    'Game': ['Trending', 'Race', 'Car', 'Bike', 'Arrow', 'Gun', 'Game','Candy crush', 'Cycle', 'Motor', 'Carton',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Battle', 'Picture', 'Country', 'City', 'Study', 
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Soccer', 'Cut', 'Live',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing', 'Exercise', 'Aeroplane', 'Plane',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Tower', 'Cutter',
    'Realtime', 'Play', 'Restaurant', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Si-fi', 'Knife',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline', 'Driving',
    'Match', 'Level', 'Card', 'Win', 'Loss', 'Runner','Board', 'Art', 'Party', 'Social', 'Color', 'Other'],

    'Sport': ['Cricket', 'Hockey', 'Match', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Hockey', 'Soccer', 
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming', 'Live',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing', 'Knife', 'Sport','Other'],

    'Social': ['Messenger', 'Chat', 'Video Chat', 'Social','Video call', 'Online', 'Offline', 'Friend',
     'Blog', 'Media Share' , 'Marketing', 'Digital marketing', 'Network', 'Game and chat', 'Movie', 'Live',
     'Funny', 'Video', 'Audio', 'Online chat', 'People', 'Class', 'Entertainment', 'Room', 'Meet','Status',
     'Comment', 'Event', 'Like', 'Share', 'Watch', 'Multi chat', 'Communication', 'Consumeer review', 'Other'],

     'Play': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Restaurant', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi', 'Other'],

    'Communication': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Restaurant', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Shop': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Restaurant', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Children': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Restaurant', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Device': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Restaurant', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],


    'Live': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Restaurant', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Top': ['Shop', 'Song', 'Technology', 'Site', 'Top','Popular', 'Communication', 'Road','Kits', 'Editor', 'Video Editor',
     'Application', 'Launcher', 'Sound','Theme', 'Cloth','Famous',  'Windows', 'Laptop', 'Live',
     'Hockey', 'Candy Crush', 'Biology', 'Math', 'Match', 'Football','Messenger',  'Coin',
    'Chat', 'Video Chat', 'Wallpaper', 'Bussiness', 'Job', 'News', 'Work', 'Battle', 'Physics', 'Book', 'Labrary', 
    'Class', 'Room', 'Reel', 'Race','Convert', 'File', 'Management', 'Movie',
     'Race', 'Car', 'Bike', 'Cycle', 'Browser','Science','Oher'],

     'Popular': ['Children', 'Cartoon', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image Editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Restaurant', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Material': ['Children', 'Cartoon', 'Restaurant', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Entertainment': ['Children', 'Cartoon', 'Restaurant', 'Keyboard', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

    'Other': ['Children', 'Cartoon', 'Keyboard', 'Restaurant', 'Mouse', 'Rat', 'Wire', 'Language', 'Speaker','Screen', 'Live',
     'Sound', 'TV', 'Mobile', 'Phone', 'Version', 'Battrey', 'Star', 'Planet', 'Earth', 'Moon', 'Zoom', 'Room',
    'Windows','Theme', 'Famous', 'Image editor', 'Laptop', 'Application', 'Launcher', 'Trending', 'Shoes',
     'Animal', 'Reading', 'Writting', 'Browser','Science', 'Shop', 'Song', 'Technology', 'Site', 'Top','Popular',
      'Communication', 'Road','Kits', 'Entertainment', 'Funny', 'Audio', 'Pool', 'Jobs', 'Labrary', 'Reel',
     'Race', 'Call', 'Car', 'Bike', 'Candy Crush', 'Cycle', 'Motor', 'Carton', 'Fan' , 'Digital marketing',
    'Circket', 'Indoor', 'Outdoor', 'Stick', 'Picture', 'Plant', 'Tree', 'Machine', 'Soccer', 'Scrol', 'Movie',
    'Basketball', 'Baseball', 'Golf', 'Volleyball', 'Ball', 'Bat', 'Badminton', 'Exercise', 'Swimming','Converter',
     'Boxing', 'Table tennis', 'Ice skating', 'Roller skating', 'Bowling', 'Horse racing', 'Snowboarding', 
     'Skateboarding', 'Archery', 'Fishing', 'Boating', 'Rock climbing', 'Rocket', 'Wrestling', 'Kickboxing',
      'Sky diving', 'Karate', 'Hanging', 'Darts', 'Surfing','Ship', 'Word', 'Plane', 'Aeroplane', 'Hot',
    'Hockey', 'Football', 'Tannis', 'Snoker', '8ballpool', 'Pool', 'Fly', 'Women', 'Men', 'Human','Town',
    'Bee', 'Quiz', 'IQ level', 'Jump', 'Walk', 'Puzzle', 'Video', 'Stund', 'Nose', 'Eye', 'Beautifull',
    'Realtime', 'Play', 'Shooter', 'Baloon', 'Action', 'Number', 'Soduku', 'Ear', 'Fishing', 'Bath',
    'Survival', 'Horror', 'Multiplayer', 'Watch', 'Role', 'Online', 'Offline','Bulb', 'Light', 'Water',
    'Match', 'Level', 'Card', 'Board', 'Art', 'Party', 'Social', 'Color', 'Country', 'Memory', 'Parts',
    'Cloth', 'City', 'Study', 'Material', 'Device', 'Engineer','Land', 'Building', 'Wifi','Other'],

 };
 
 // When an option is changed, search the above for matching choices
 $('#options').on('change', function() {
    // Set selected option as variable
    var selectValue = $(this).val();
 
    // Empty the target field
    $('#choices').empty();
    
    // For each chocie in the selected option
    for (i = 0; i < lookup[selectValue].length; i++) {
       // Output choice in the target field
       $('#choices').append("<option value='" + lookup[selectValue][i] + "'>" + lookup[selectValue][i] + "</option>");
    }
 });






