from django.db import migrations

def seed_quotes(apps, schema_editor):
    Quote = apps.get_model('quotes', 'Quote')
    quotes = [
        {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
        {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
        {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
        {"text": "Fix the cause, not the symptom.", "author": "Steve Maguire"},
    ]
    for q in quotes:
        Quote.objects.create(text=q["text"], author=q["author"])

class Migration(migrations.Migration):
    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_quotes),
    ]