import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_dict = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_dict["name"],
            defaults={
                "description": race_dict["description"],
            }
        )

        for skill_dict in race_dict["skills"]:
            Skill.objects.get_or_create(
                name=skill_dict["name"],
                defaults={
                    "bonus": skill_dict["bonus"],
                    "race": race,
                }
            )

        guild_dict = player_data["guild"]
        if guild_dict:
            guild, _ = Guild.objects.get_or_create(
                name=guild_dict["name"],
                defaults={
                    "description": guild_dict["description"],
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
