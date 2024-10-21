from fractions import Fraction
from copy import deepcopy

character='Crusader'

weights={
    'Dexterity':40,
    'Intelligence':40,
    'Strength':40,
    'Vitality':40,
    'Area Damage':10,
    'Attack Speed':10,
    'Critical Hit Chance':10,
    'Critical Hit Damage':10,
    'Critical Hit Damage (Weapon)':1,
    'Damage %':10,
    'Damage to Elites':1,
    '+ Damage (Off-Hand)':1000,
    '+ Damage':100,
    '+ Fire Damage':100,
    '+ Cold Damage':100,
    '+ Poison Damage':100,
    '+ Arcane Damage':100,
    '+ Lightning Damage':100,
    '+ Holy Damage':100,
    '+ Damage (finery)':15,
    'Arcane Skill Damage':10,
    'Cold Skill Damage':10,
    'Fire Skill Damage':10,
    'Holy Skill Damage':10,
    'Lightning Skill Damage':10,
    'Physical Skill Damage':10,
    'Poison Skill Damage':10,
    'Cooldown Reduction':10,
    'Resource Cost Reduction':10,
    'Life %':10,
    'Life per Hit':10,
    'Life per Second':10,
    'Globe Healing':10,
    'Life per Kill':10,
    'Block Chance':10,
    'Armor':10,
    'Reduced Damage Cold':10,
    'Reduced Damage Elites':1,
    'Reduced Crowd Control':10,
    'Reduced Damage Melee':4,
    'Reduced Damage Range':4,
    'Thorns':6,
    'Resistance to All':10,
    'Arcane Resistance':10,
    'Cold Resistance':10,
    'Fire Resistance':10,
    'Lightning Resistance':10,
    'Physical Resistance':10,
    'Poison Resistance':10,
    'Movement Speed':20,
    'Sockets':10,
    'Bonus XP per Kill':10,
    'Bonus XP %':10,
    'Gold Find':10,
    'Magic Find':10,
    'Pickup Radius':15,
    'Level Requirement Reduced':1,
    'Ignore Durability Loss':1,
    'Chance to Bleed':1,
    'Chance to Blind':1,
    'Chance to Chill':1,
    'Chance to Fear (Weapon)':1,
    'Chance to Fear (Helmet)':2,
    'Chance to Freeze':1,
    'Chance to Immobilize':1,
    'Chance to Knockback':1,
    'Chance to Slow':1,
    'Chance to Stun':1,
    'Life per Fury spent':20,
    'Max Fury':40,
    'Life per Wrath spent':1,
    'Wrath Regeneration':10,
    'Max Wrath':40,
    'Hatred Regeneration':20,
    'Max Discipline':40,
    'Life per Spirit spent':20,
    'Spirit Regeneration':20,
    'Max Spirit':40,
    'Mana Regeneration':20,
    'Max Mana':20,
    'Arcane Power on Crit':40,
    'Max Arcane Power':40,
    'Max Essence':40,
    'S Cleave':10,
    'S Weapon Throw':10,
    'S Frenzy':10,
    'S Bash':10,
    'S Ancient Spear':10,
    'S Hammer of the Ancients':10,
    'S Whirlwind':10,
    'S Seismic Slam':10,
    'S Furious Charge':10,
    'S Avalanche':10,
    'S Earthquake':10,
    'S Rend':10,
    'S Revenge':10,
    'S Overpower':10,
    'S Call of the Ancients':10,
    'S Justice':10,
    'S Punish':10,
    'S Smite':10,
    'S Slash':10,
    'S Blessed Shield':10,
    'S Shield Bash':10,
    'S Phalanx':10,
    'S Blessed Hammer':10,
    'S Fist of Heavens':10,
    'S Sweep Attack':10,
    'S Condemn':10,
    'S Heaven\'s Fury':10,
    'S Falling Sword':10,
    'S Bombardment':10,
    'S Hungering Arrow':10,
    'S Bolas':10,
    'S Entangling Shot':10,
    'S Grenade':10,
    'S Evasive Fire':10,
    'S Chakram':10,
    'S Impale':10,
    'S Rapid Fire':10,
    'S Elemental Arrow':10,
    'S Strafe':10,
    'S Cluster Arrow':10,
    'S Multishot':10,
    'S Fan of Knives':10,
    'S Companion':10,
    'S Spike Trap':10,
    'S Rain of Vengeance':10,
    'S Sentry':10,
    'S Deadly Reach':10,
    'S Way of the Hundred Fists':10,
    'S Fists of Thunder':10,
    'S Crippling Wave':10,
    'S Exploding Palm':10,
    'S Wave of Light':10,
    'S Tempest Rush':10,
    'S Lashing Tail Kick':10,
    'S Sweeping Wind':10,
    'S Cyclone Strike':10,
    'S Mystic Ally':10,
    'S Dashing Strike':10,
    'S Seven-Sided Strike':10,
    'S Plague of Toads':10,
    'S Firebomb':10,
    'S Poison Dart':10,
    'S Corpse Spiders':10,
    'S Zombie Charger':10,
    'S Sacrifice':10,
    'S Firebats':10,
    'S Acid Cloud':10,
    'S Spirit Barrage':10,
    'S Locust Swarm':10,
    'S Grasp of the Dead':10,
    'S Summon Zombie Dogs':10,
    'S Wall of Death':10,
    'S Gargantuan':10,
    'S Haunt':10,
    'S Piranhas':10,
    'S Fetish Army':10,
    'S Magic Missile':10,
    'S Shock Pulse':10,
    'S Electrocute':10,
    'S Spectral Blade':10,
    'S Disintegrate':10,
    'S Arcane Torrent':10,
    'S Arcane Orb':10,
    'S Ray of Frost':10,
    'S Energy Twister':10,
    'S Wave of Force':10,
    'S Meteor':10,
    'S Explosive Blast':10,
    'S Familiar':10,
    'S Black Hole':10,
    'S Hydra':10,
    'S Blizzard':10,
    'S Bone Spikes':10,
    'S Grim Scythe':10,
    'S Siphon Blood':10,
    'S Bone Spear':10,
    'S Death Nova':10,
    'S Skeletal Mage':10,
    'S Command Skeletons':10,
    'S Command Golem':10,
    'S Revive':10,
    'S Bone Armor':10,
    'S Bone Spirit':10,
    'S Corpse Explosion':10,
    'S Corpse Lance':10}
weights_backup=weights.copy()

elemental_skill=frozenset({
    'Arcane Skill Damage',
    'Cold Skill Damage',
    'Fire Skill Damage',
    'Holy Skill Damage',
    'Lightning Skill Damage',
    'Physical Skill Damage',
    'Poison Skill Damage'})

weapon_damage=frozenset({
    '+ Damage',
    '+ Fire Damage',
    '+ Cold Damage',
    '+ Poison Damage',
    '+ Arcane Damage',
    '+ Lightning Damage',
    '+ Holy Damage'})

resistances=frozenset({
    'Arcane Resistance',
    'Cold Resistance',
    'Fire Resistance',
    'Lightning Resistance',
    'Physical Resistance',
    'Poison Resistance',
    'Resistance to All'})

chance_on_hit=frozenset({
    'Chance to Blind',
    'Chance to Chill',
    'Chance to Fear (Weapon)',
    'Chance to Freeze',
    'Chance to Immobilize',
    'Chance to Knockback',
    'Chance to Slow',
    'Chance to Stun'})

skill_damage=frozenset({
    'S Cleave',
    'S Weapon Throw',
    'S Frenzy',
    'S Bash',
    'S Ancient Spear',
    'S Hammer of the Ancients',
    'S Whirlwind',
    'S Seismic Slam',
    'S Furious Charge',
    'S Avalanche',
    'S Earthquake',
    'S Rend',
    'S Revenge',
    'S Overpower',
    'S Call of the Ancients',
    'S Justice',
    'S Punish',
    'S Smite',
    'S Slash',
    'S Blessed Shield',
    'S Shield Bash',
    'S Phalanx',
    'S Blessed Hammer',
    'S Fist of Heavens',
    'S Sweep Attack',
    'S Condemn',
    'S Heaven\'s Fury',
    'S Falling Sword',
    'S Bombardment',
    'S Hungering Arrow',
    'S Bolas',
    'S Entangling Shot',
    'S Grenade',
    'S Evasive Fire',
    'S Chakram',
    'S Impale',
    'S Rapid Fire',
    'S Elemental Arrow',
    'S Strafe',
    'S Cluster Arrow',
    'S Multishot',
    'S Fan of Knives',
    'S Companion',
    'S Spike Trap',
    'S Rain of Vengeance',
    'S Sentry',
    'S Deadly Reach',
    'S Way of the Hundred Fists',
    'S Fists of Thunder',
    'S Crippling Wave',
    'S Exploding Palm',
    'S Wave of Light',
    'S Tempest Rush',
    'S Lashing Tail Kick',
    'S Sweeping Wind',
    'S Cyclone Strike',
    'S Mystic Ally',
    'S Dashing Strike',
    'S Seven-Sided Strike',
    'S Plague of Toads',
    'S Firebomb',
    'S Poison Dart',
    'S Corpse Spiders',
    'S Zombie Charger',
    'S Sacrifice',
    'S Firebats',
    'S Acid Cloud',
    'S Spirit Barrage',
    'S Locust Swarm',
    'S Grasp of the Dead',
    'S Summon Zombie Dogs',
    'S Wall of Death',
    'S Gargantuan',
    'S Haunt',
    'S Piranhas',
    'S Fetish Army',
    'S Magic Missile',
    'S Shock Pulse',
    'S Electrocute',
    'S Spectral Blade',
    'S Disintegrate',
    'S Arcane Torrent',
    'S Arcane Orb',
    'S Ray of Frost',
    'S Energy Twister',
    'S Wave of Force',
    'S Meteor',
    'S Explosive Blast',
    'S Familiar',
    'S Black Hole',
    'S Hydra',
    'S Blizzard',
    'S Bone Spikes',
    'S Grim Scythe',
    'S Siphon Blood',
    'S Bone Spear',
    'S Death Nova',
    'S Skeletal Mage',
    'S Command Skeletons',
    'S Command Golem',
    'S Revive',
    'S Bone Armor',
    'S Bone Spirit',
    'S Corpse Explosion',
    'S Corpse Lance'})

life_per_trigger=frozenset({
    'Life per Hit',
    'Life per Kill'
    })

exclusion_classes=frozenset({
    elemental_skill,
    weapon_damage,
    resistances,
    chance_on_hit,
    skill_damage,
    life_per_trigger
    })

mainhand_types=frozenset({
    'Axe',
    'Dagger',
    'Mace',
    'Spear',
    'Sword',
    'Mighty Weapon',
    'Flail',
    'Hand Crossbow',
    'Fist Weapon',
    'Ceremonial Knife',
    'Wand',
    '2H Axe',
    '2H Mace',
    'Polearm',
    '2H Sword',
    '2H Mighty Weapon',
    '2H Flail',
    'Bow',
    'Crossbow',
    'Staff',
    'Daibo',
    'Scythe',
    '2H Scythe'})

offhand_types=frozenset({
    'Mojo',
    'Quiver',
    'Source',
    'Phylactery'})

weapon_types=mainhand_types|offhand_types

jewelry_types=frozenset({'Ring','Amulet'})

def update_prob(preprob,selected,pool):
    num=weights[selected]
    den=sum(weights[x] for x in pool)
    return preprob*Fraction(num,den)

def update_pool(selected,prepool):
    pool=prepool.copy()
    pool.discard(selected)
    for c in exclusion_classes:
        if selected in c:
            for x in c:
                pool.discard(x)
    return pool

def mainstat():
    if character in {'Crusader','Barbarian'}:
        return 'Strength'
    if character in {'Witch Doctor','Wizard','Necromancer'}:
        return 'Intelligence'
    if character in {'Monk','Demon Hunter'}:
        return 'Dexterity'
    else:
        raise NameError('Invalid character class')

def elements():
    if character in {'Barbarian','Demon Hunter'}:
        return {'Physical Skill Damage','Fire Skill Damage','Cold Skill Damage','Lightning Skill Damage'}
    if character=='Crusader':
        return {'Holy Skill Damage','Lightning Skill Damage','Fire Skill Damage','Physical Skill Damage'}
    if character=='Monk':
        return {'Holy Skill Damage','Lightning Skill Damage','Cold Skill Damage','Fire Skill Damage','Physical Skill Damage'}
    if character=='Witch Doctor':
        return {'Poison Skill Damage','Fire Skill Damage','Cold Skill Damage','Physical Skill Damage'}
    if character=='Wizard':
        return {'Lightning Skill Damage','Fire Skill Damage','Cold Skill Damage','Arcane Skill Damage'}
    if character=='Necromancer':
        return {'Cold Skill Damage','Physical Skill Damage','Poison Skill Damage'}
    else:
        raise NameError('Invalid character class')

def skills(group):
    if group==1 and character=='Barbarian':
        return {'S Cleave','S Weapon Throw','S Frenzy','S Bash',}
    if group==2 and character=='Barbarian':
        return {'S Ancient Spear','S Hammer of the Ancients','S Whirlwind','S Seismic Slam'}
    if group==3 and character=='Barbarian':
        return {'S Furious Charge','S Avalanche','S Earthquake','S Rend','S Revenge','S Overpower','S Call of the Ancients'}
    if group==1 and character=='Crusader':
        return {'S Justice','S Punish','S Smite','S Slash'}
    if group==2 and character=='Crusader':
        return {'S Blessed Shield','S Shield Bash','S Phalanx','S Blessed Hammer','S Fist of Heavens','S Sweep Attack'}
    if group==3 and character=='Crusader':
        return {'S Condemn','S Heaven\'s Fury','S Falling Sword','S Bombardment'}
    if group==1 and character=='Demon Hunter':
        return {'S Hungering Arrow','S Bolas','S Entangling Shot','S Grenade','S Evasive Fire'}
    if group==2 and character=='Demon Hunter':
        return {'S Chakram','S Impale','S Rapid Fire','S Elemental Arrow','S Strafe','S Cluster Arrow','S Multishot'}
    if group==3 and character=='Demon Hunter':
        return {'S Fan of Knives','S Companion','S Spike Trap','S Rain of Vengeance','S Sentry'}
    if group==1 and character=='Monk':
        return {'S Deadly Reach','S Way of the Hundred Fists','S Fists of Thunder','S Crippling Wave'}
    if group==2 and character=='Monk':
        return {'S Exploding Palm','S Wave of Light','S Tempest Rush','S Lashing Tail Kick'}
    if group==3 and character=='Monk':
        return {'S Sweeping Wind','S Cyclone Strike','S Mystic Ally','S Dashing Strike','S Seven-Sided Strike'}
    if group==1 and character=='Witch Doctor':
        return {'S Plague of Toads','S Firebomb','S Poison Dart','S Corpse Spiders'}
    if group==2 and character=='Witch Doctor':
        return {'S Zombie Charger','S Sacrifice','S Firebats','S Acid Cloud','S Spirit Barrage'}
    if group==3 and character=='Witch Doctor':
        return {'S Locust Swarm','S Grasp of the Dead','S Summon Zombie Dogs','S Wall of Death','S Gargantuan','S Haunt','S Piranhas','S Fetish Army'}
    if group==1 and character=='Wizard':
        return {'S Magic Missile','S Shock Pulse','S Electrocute','S Spectral Blade'}
    if group==2 and character=='Wizard':
        return {'S Disintegrate','S Arcane Torrent','S Arcane Orb','S Ray of Frost','S Energy Twister','S Wave of Force','S Meteor'}
    if group==3 and character=='Wizard':
        return {'S Explosive Blast','S Familiar','S Black Hole','S Hydra','S Blizzard'}
    if group==1 and character=='Necromancer':
        return {'S Bone Spikes','S Grim Scythe','S Siphon Blood'}
    if group==2 and character=='Necromancer':
        return {'S Bone Spear','S Death Nova','S Skeletal Mage'}
    if group==3 and character=='Necromancer':
        return {'S Command Skeletons','S Command Golem','S Revive','S Bone Armor','S Bone Spirit','S Corpse Explosion','S Corpse Lance'}
    if group not in {1,2,3}:
        raise NameError('Invalid skill group number.')
    else:
        raise NameError('Invalid character class.')

def primaries(type):
    pool={mainstat(),'Vitality'}
    if type not in weapon_types:
        pool.update({'Resistance to All','Armor'})
        if type in {'Helm','Spirit Stone','Voodoo Mask','Wizard Hat'}:
            pool.update({'Sockets','Life %','Life per Second','Life per Hit','Critical Hit Chance'}|skills(2))
            if type=='Spirit Stone':
                pool.update({'Life per Spirit spent','Spirit Regeneration'})
            elif type=='Voodoo Mask':
                pool.update({'Mana Regeneration'})
            elif type=='Wizard Hat':
                pool.update({'Arcane Power on Crit'})
        elif type=='Shoulders':
            pool.update({'Life %','Life per Second','Cooldown Reduction','Area Damage','Resource Cost Reduction'}|skills(3))
        elif type=='Gloves':
            pool.update({'Life per Second','Life per Hit','Attack Speed','Critical Hit Chance','Critical Hit Damage','Cooldown Reduction','Area Damage','Resource Cost Reduction'})
        elif type in {'Chest Armor','Cloak'}:
            pool.update({'Sockets','Reduced Damage Elites','Life %','Life per Second'}|skills(3))
            if type=='Cloak':
                pool.update({'Hatred Regeneration'})
        elif type in {'Belt','Mighty Belt'}:
            pool.update({'Life %','Life per Second'}|skills(1))
            if type=='Mighty Belt':
                pool.update({'Life per Fury spent'})
        elif type=='Pants':
            pool.update({'Sockets','Life per Second'}|skills(1))
        elif type=='Boots':
            pool.update({'Life per Second','Movement Speed'}|skills(2))
        elif type=='Bracers':
            pool.update({'Life per Second','Life per Hit','Critical Hit Chance'}|elements())
        elif type=='Ring':
            pool.update({'Sockets','+ Damage (finery)','Life %','Life per Second','Life per Hit','Attack Speed','Critical Hit Chance','Critical Hit Damage','Area Damage','Cooldown Reduction','Resource Cost Reduction'})
        elif type=='Amulet':
            pool.update({'Sockets','+ Damage (finery)','Life %','Life per Second','Life per Hit','Attack Speed','Critical Hit Chance','Critical Hit Damage','Area Damage','Cooldown Reduction','Resource Cost Reduction'}|elements())
        elif type in {'Shield','Crusader Shield'}:
            pool.update({'Sockets','Block Chance','Reduced Damage Elites','Life %','Life per Second','Critical Hit Chance','Cooldown Reduction','Resource Cost Reduction','Damage to Elites','Chance to Bleed'})
            if type=='Crusader Shield':
                pool.update({'Life per Wrath spent','Area Damage','Wrath Regeneration'}|skills(1)|skills(2)|skills(3))
        pass # Follower Items Here
    else:
        pool.update({'Sockets','Area Damage','Cooldown Reduction','Damage to Elites','Chance to Bleed','Resource Cost Reduction'})
        if type not in {'Mojo','Quiver','Source','Phylactery'}:
            pool.update({'Life per Hit','Damage %','Attack Speed'}|weapon_damage)
            if type=='Ceremonial Knife':
                pool.update({'Mana Regeneration'})
            elif type in {'Fist Weapon','Daibo'}:
                pool.update({'Life per Spirit spent','Spirit Regeneration'})
                if type=='Daibo':
                    pool.update(set(skills(1)|skills(2)|skills(3)))
            elif type=='Hand Crossbow':
                pool.update({'Hatred Regeneration'})
            elif type in {'Flail', '2H Flail'}:
                pool.update({'Life per Wrath spent','Wrath Regeneration'})
            elif type in {'Mighty Weapon','2H Mighty Weapon'}:
                pool.update({'Life per Fury spent'})
                if type=='2H Mighty Weapon':
                    pool.update(set(skills(1)|skills(2)|skills(3)))
        else:
            pool.update({'Life %','Life per Second','Critical Hit Chance'}|skills(1)|skills(2)|skills(3))
            if type=='Mojo':
                pool.update({'Mana Regeneration'})
            if type=='Quiver':
                pool.update({'Hatred Regeneration'})
            if type=='Source':
                pool.update({'Arcane Power on Crit'})
    if len(pool)<5:
        print('Type not recognized. Check for typing errors.')
        return None
    return pool

def secondaries(type):
    pool={'Bonus XP per Kill'}
    if type not in mainhand_types:
        pool.update({'Gold Find','Thorns'})
    if type not in weapon_types|jewelry_types|{'Shield','Crusader Shield'}:
        pool.add('Pickup Radius')
    if type not in jewelry_types:
        pool.update({'Level Requirement Reduced','Ignore Durability Loss'})
    if type not in weapon_types:
        pool.update(resistances-{'Resistance to All'})
    if type in {'Helm','Spirit Stone','Voodoo Mask','Wizard Hat'}|jewelry_types|{'Shield','Crusader Shield'}:
        pool.add('Reduced Crowd Control')
    if type in {'Chest Armor','Cloak','Bracers','Amulet','Shield','Crusader Shield'}:
        pool.update({'Reduced Damage Melee','Reduced Damage Range'})
    if type in {'Chest Armor','Cloak','Boots','Shoulders','Shield','Crusader Shield'}|jewelry_types|offhand_types:
        pool.add('Globe Healing')
    if type in {'Chest Armor','Cloak','Belt','Mighty Belt','Pants'}|jewelry_types|mainhand_types:
        pool.add('Life per Kill')
    if type in {'Shield','Crusader Shield'}|weapon_types:
        pool.update(chance_on_hit)
    if type in {'Helm','Spirit Stone','Voodoo Mask','Wizard Hat'}: pool.add('Chance to Fear (Helmet)')
    if type in {'Belt','Mighty Belt'}: pool.add('Chance to Freeze')
    if type=='Pants': pool.add('Chance to Slow')
    if type=='Gloves': pool.add('Chance to Stun')
    if type=='Boots': pool.add('Chance to Immobilize')
    if type=='Bracers': pool.add('Chance to Knockback')
    if type=='Shoulders': pool.add('Chance to Chill')
    if type=='Amulet': pool.add('Chance to Blind')
    if type in {'Spirit Stone','Fist Weapon','Daibo'}: pool.add('Max Spirit')
    if type in {'Voodoo Mask','Mojo','Ceremonial Knife'}: pool.add('Max Mana')
    if type in {'Wizard Hat','Source','Wand'}: pool.add('Max Arcane Power')
    if type in {'Cloak','Quiver','Hand Crossbow'} or (type in {'Bow','Crossbow'} and character=='Demon Hunter'): pool.add('Max Discipline')
    if type in {'Mighty Belt','Mighty Weapon','2H Mighty Weapon'}: pool.add('Max Fury')
    if type in {'Flail','2H Flail','Crusader Shield'}: pool.add('Max Wrath')
    if type in {'Scythe','2H Scythe','Phylactery'}: pool.add('Max Essence')
    return pool

items={
    'Andariel\'s Visage':[[{mainstat()},1],[{'Attack Speed'},1],[elements(),1],[primaries('Helm'),1]],
    'Blind Faith':[[{mainstat()},1],[{'Chance to Blind'},1],[primaries('Helm'),3],[secondaries('Helm'),1]],
    'Broken Crown':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),1]],
    'Deathseer\'s Cowl':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),1]],
    'The Helm of Rule':[[{'Vitality'},1],[{'Block Chance'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Leoric\'s Crown':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),1]],
    'Mempo of Twilight':[[{mainstat()},1],[{'Sockets'},1],[{'Resistance to All'},1],[{'Attack Speed'},1],[secondaries('Helm'),2]],
    'Pride\'s Fall':[[{mainstat()},1],[{'Vitality'},1],[{'Critical Hit Chance'},1],[primaries('Helm'),1],[secondaries('Helm'),1]],
    'Skull of Resonance':[[{mainstat()},1],[{'Sockets'},1],[{'Resistance to All'},1],[primaries('Helm'),1],[secondaries('Helm'),1]],
    'Visage of Gunes':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),1]],
    'Warhelm of Kassar':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),1]],
    'Accursed Visage':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Aughild\'s Spike':[[{'Resistance to All'},1],[primaries('Helm'),3],[secondaries('Helm'),2]],
    'Cain\'s Insight':[[{'Bonus XP per Kill'},1],[primaries('Helm'),4],[secondaries('Helm'),1]],
    'Eyes of the Earth':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Guardian\'s Gaze':[[{'Movement Speed'},1],[primaries('Helm'),4],[secondaries('Helm'),1]],
    'Immortal King\'s Triumph':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Jade Harvester\'s Wisdom':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Marauder\'s Visage':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Natalya\'s Sight':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Sage\'s Apogee':[[{'Sockets'},1],[primaries('Helm'),3],[secondaries('Helm'),2]],
    'The Shadow\'s Mask':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Sunwuko\'s Crown':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Tal Rasha\'s Guise of Wisdom':[[{mainstat()},1],[{'Sockets'},1],[{'Critical Hit Chance'},1],[primaries('Helm'),1],[secondaries('Helm'),2]],
    'Vyr\'s Sightless Skull':[[{mainstat()},1],[{'Sockets'},1],[primaries('Helm'),2],[secondaries('Helm'),2]],
    'Jesseth Skullscythe':[[{mainstat()},1],[set(weapon_damage),1],[{'Attack Speed'},1],[primaries('Scythe'),1],[secondaries('Scythe'),2]],
    'Pig Sticker':[[{mainstat()},1],[set(weapon_damage),1],[primaries('Dagger'),3]],
    'The Flavor of Time':[[{'Movement Speed'},1],[{'Cooldown Reduction'},1],[primaries('Amulet'),3],[secondaries('Amulet'),1]]
    }

# def set_character(char):
#     if char not in {'Barbarian','Crusader','Demon Hunter','Monk','Witch Doctor','Wizard','Necromancer'}:
#         print('Typing Error. Check for typos and capitalize each word.')
#         return None
#     global character
#     character=char
#     return None

def assume_uniform():
    """
    Set affix weights except weapon damage and attributes to be uniform.

    Returns
    -------
    None.

    """
    global weights
    for affix in weights:
        weights[affix]=1
    for attribute in {'Dexterity','Strength','Intelligence','Vitality'}:
        weights[attribute]=4
    for d in weapon_damage:
        weights[d]=10

def restore_datamined():
    """
    Set affix weights to the values from the datamined source.

    Returns
    -------
    None.

    """
    global weights
    weights=weights_backup

def distribution(item : str) -> dict[frozenset,Fraction]:
    """
    Compute the probability distribution over all complete affix combinations
    for the given item.

    Parameters
    ----------
    item : str
        Name of the item. It needs to be defined in the global dict 'items'.

    Returns
    -------
    dict[frozenset,Fraction]
        affix combination -> probability

    """
    inst=deepcopy(items[item])
    dist=dict()
    def proceed(trace,instr,prob):
        if instr==[]:
            nonlocal dist
            comb=frozenset(trace)
            if comb in dist: dist[comb]+=prob
            else: dist[comb]=prob
        else:
            for x in instr[0][0]:
                p=update_prob(prob,x,instr[0][0])
                t=deepcopy(trace)+[x]
                i=deepcopy(instr)
                for s in i:
                    s[0]=update_pool(x,s[0])
                i[0][1]-=1
                if i[0][1]==0: i=i[1:]
                proceed(t,i,p)
    proceed([],inst,Fraction(1,1))
    return dist

def check_enchantable(config : tuple[str], item : str, type : str) -> Fraction:
    """
    Compute the probability that a given item generates with any affix combination
    that can be enchanted into the desired configuration,
    i.e. is off by at most one affix.

    Parameters
    ----------
    config : tuple[str]
        all demanded affixes
    item : str
        name of the item
    type : str
        type of the item

    Returns
    -------
    Fraction
        probability to be enchantable into the configuration.

    """
    d=distribution(item)
    p=Fraction(0)
    c=set(config)
    for x in d:
        if c-x==set(): p+=d[x]
        elif len(c-x)==1:
            a=(c-x).pop()
            s=''
            if a in primaries(type): s='primary'
            elif a in secondaries(type): s='secondary'
            else: return "Error: invalid affixes for type. "+str(a)
            r=False
            for y in x:
                if s=='primary' and y in primaries(type):
                    pool=primaries(type)
                    for z in x-{y}:
                        pool=update_pool(z,pool)
                    if a in pool: r=True
                if s=='secondary' and y in secondaries(type):
                    pool=secondaries(type)
                    for z in x-{y}:
                        pool=update_pool(z,pool)
                    if a in pool: r=True
            if r: p+=d[x]
    return p
