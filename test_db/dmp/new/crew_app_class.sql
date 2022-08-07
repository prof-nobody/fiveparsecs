UPDATE public.crew_app_class SET roll = '[1,5)', name = 'Working Class', effect = '{+1 Savvy,+1 Luck}', resources = '', starting_rolls = '' WHERE id = 1;
UPDATE public.crew_app_class SET roll = '[6,9)', name = 'Technician', effect = '{+1 Savvy}', resources = '', starting_rolls = '{+1 Gear}' WHERE id = 2;
UPDATE public.crew_app_class SET roll = '[10,13)', name = 'Scientist', effect = '{+1 Savvy}', resources = '', starting_rolls = '{+1 Gadget}' WHERE id = 3;
UPDATE public.crew_app_class SET roll = '[14,17)', name = 'Hacker', effect = '{+1 Savvy}', resources = '{Rival}', starting_rolls = '' WHERE id = 4;
UPDATE public.crew_app_class SET roll = '[18,22)', name = 'Soldier', effect = '{+1 Combat Skill}', resources = '{+1d6 Credits}', starting_rolls = '' WHERE id = 5;
UPDATE public.crew_app_class SET roll = '[23,27)', name = 'Mercenary', effect = '{+1 Combat Skill}', resources = '', starting_rolls = '{+1 Military Weapon}' WHERE id = 6;
