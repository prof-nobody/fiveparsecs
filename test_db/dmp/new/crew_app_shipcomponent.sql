UPDATE public.crew_app_shipcomponent SET name = 'Medical Bay', description = 'Fully stocked medical facility to aid long-term recovery. Each campaign turn when recovering from Injuries, select a crew member who can mark off 2 campaign turns of recovery.', traits = null, cost = 25 WHERE id = 2;
UPDATE public.crew_app_shipcomponent SET name = 'Cargo Hold', description = 'The hold of the ship has been upgraded to be environmentally stable. When traveling to a new planet, you may take on cargo. Roll 2D6 and discard any 5-6. Select the highest remaining die and ear that many credits from delivering a shipment to the new world. If both dice are discarded, no shipments are available. If your ship is damaged in transit, the cargo is also lost.', traits = null, cost = 15 WHERE id = 3;
UPDATE public.crew_app_shipcomponent SET name = 'Database', description = 'Extensive data records have been added to aid in decision making. When traveling to a new planet, you may roll up the details for one additional planet, and then select which to visit.', traits = null, cost = 10 WHERE id = 4;
UPDATE public.crew_app_shipcomponent SET name = 'Shuttle', description = 'Launch bay with a standard "Lemon Shark" shuttle for quick deployments. If you receive the Distress Call Starship Travel event, you may roll twice and pick the higher roll. If a planet is Invaded, you may add +2 to the roll to get off-world.', traits = null, cost = 15 WHERE id = 5;