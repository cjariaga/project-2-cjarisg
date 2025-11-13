"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Clayan Ariaga
Date: 11/07/2025

AI Usage: AI helped with debugging, better explanation, and code errors such as syntax errors.
"""
#c
# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """

    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")

        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)

        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()

        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

import random

class Character:
    """Base class for all characters."""

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """Basic physical attack."""
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        """Reduces health but not below 0."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")

    def display_stats(self):
        """Displays basic character stats."""
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


class Player(Character):
    """Base class for player characters."""

    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """Displays player stats with additional info."""
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | XP: {self.experience}")


class Warrior(Player):
    """Strong physical fighter."""

    def __init__(self, name):
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        """Warrior attack with bonus damage."""
        damage = self.strength + 5
        print(f"{self.name} swings a mighty sword for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """Special attack: big hit."""
        damage = self.strength + 15
        print(f"{self.name} uses POWER STRIKE! Deals {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """Magical spellcaster."""

    def __init__(self, name):
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        """Magic-based basic attack."""
        damage = self.magic
        print(f"{self.name} casts a magic bolt for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """Special magical ability."""
        damage = self.magic + 10
        print(f"{self.name} casts FIREBALL for {damage} damage!")
        target.take_damage(damage)


class Rogue(Player):
    """Quick and sneaky fighter."""

    def __init__(self, name):
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        """Chance for critical hit."""
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage = self.strength * 2
            print(f"💥 Critical hit! {self.name} deals {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} slashes swiftly for {damage} damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """Guaranteed critical hit."""
        damage = self.strength * 2
        print(f"{self.name} performs a SNEAK ATTACK 🗡️ for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    """Represents a weapon (composition)."""

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: +{self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Polymorphism test
    print("\n⚔️ Testing Polymorphism:")
    dummy = Character("Target Dummy", 100, 0, 0)
    for c in [warrior, mage, rogue]:
        print(f"\n{c.name} attacks the dummy:")
        c.attack(dummy)
        dummy.health = 100  # Reset dummy

    # Special abilities
    print("\n✨ Testing Special Abilities:")
    t1 = Character("Enemy1", 50, 0, 0)
    t2 = Character("Enemy2", 50, 0, 0)
    t3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(t1)
    mage.fireball(t2)
    rogue.sneak_attack(t3)

    # Weapon test
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Battle system test
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
