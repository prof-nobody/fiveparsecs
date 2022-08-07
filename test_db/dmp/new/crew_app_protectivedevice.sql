UPDATE public.crew_app_protectivedevice SET name = 'Battle Dress', category = 'AR', equippable = true, description = 'The character counts as +1 Reactions (maximum 4) and receives a Saving Throw of 5+.' WHERE id = 1;
UPDATE public.crew_app_protectivedevice SET name = 'Camo Cloak', category = 'SC', equippable = true, description = 'If character is within 2" of Cover, they are counted as being in Cover. Does not apply if the shooter is within 4".' WHERE id = 2;
UPDATE public.crew_app_protectivedevice SET name = 'Combat Armor', category = 'AR', equippable = true, description = 'Saving Throw 5+' WHERE id = 3;
UPDATE public.crew_app_protectivedevice SET name = 'Deflector Shield', category = 'SC', equippable = true, description = 'Automatically deflect a single ranged weapon''s Hit per battle. After a Hit is scored, decide if you with to use the field before any rolls for Toughness or armor are made.' WHERE id = 4;
UPDATE public.crew_app_protectivedevice SET name = 'Flak Screen', category = 'SC', equippable = true, description = 'All Area weapons striking the wearer, whether through the initial shots or additional attacks from the Area trait have their Damage reduced by -1 (to a cap of +0).' WHERE id = 5;
UPDATE public.crew_app_protectivedevice SET name = 'Flex-armor', category = 'AR', equippable = true, description = 'If the character did not move on their last activation, they countas +1 Toughness (to a maximum of 6).' WHERE id = 6;
UPDATE public.crew_app_protectivedevice SET name = 'Frag Vest', category = 'AR', equippable = true, description = 'The wearer receives a 6+ Saving Throw. Improved to 5+ against Area attacks.' WHERE id = 8;
UPDATE public.crew_app_protectivedevice SET name = 'Stealth Gear', category = 'AR', equippable = true, description = 'Enemies firing from a range over 9" are -1 to Hit.' WHERE id = 7;