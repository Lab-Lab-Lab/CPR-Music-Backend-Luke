# Generated by Django 3.2.11 on 2024-03-15 19:47

from django.db import migrations

def fix_instructions(apps, schema_editor):
    Activity = apps.get_model("assignments", "Activity")
    ActivityCategory = apps.get_model("assignments", "ActivityCategory")
    ActivityType = apps.get_model("assignments", "ActivityType")
    PartType = apps.get_model("musics", "PartType")
    
    melody = PartType.objects.get(name="Melody")

    create_ctgy = ActivityCategory.objects.get(name="Create")
    act_type, act_t_created = ActivityType.objects.update_or_create(
        name='Exploratory',
        category=create_ctgy,
    )
    exploratory, e_created = Activity.objects.get_or_create(
        activity_type=act_type,
        part_type=melody,
        activity_type_name=act_type.name,
        category=create_ctgy.name
    )
    exploratory.body='<h3>INSTRUCTIONS</h3><ol><li>Write three, one-bar motives using the note bins provided. You may use half notes, quarter notes, eighth notes, and rests. When you have written all three motives, select "Begin Composing." The computer will generate variations of your motives which you can use in the next step. The generated variations will be grouped under tabs labeled with the bin name (e.g. "Tonic").</li><li>Draft your melody by:<ol><li>Choosing a bin and clicking its tab to see your motive along with the generated variations.<ul><li>NOTE: The blank staff is color-coordinated with the motives (red, green, and blue).</li></ul></li><li>Find a your preferred measure in in the Variations tab and click anywhere in that measure.</li><li>Click in a measure in the blank staff into which you want the notes to be copied.</li></ol><li>You may edit your final composition draft if you wish.</li><li>Record your composition and submit for review.<ul><li>NOTE: When you click the record (microphone) button, the accompaniment track will play. The accompaniment track provides two measures of rest. Wait until the third measure before you begin playing your melody.</li></ul></li></ol>'
    exploratory.save()


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0033_auto_20240312_2321'),
    ]

    operations = [
        migrations.RunPython(fix_instructions, migrations.RunPython.noop),
    ]