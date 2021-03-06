# Generated by Django 2.2.26 on 2022-03-24 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rango.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_text', models.CharField(max_length=4096)),
                ('country', models.CharField(choices=[('ï»¿afg', 'Afghanistan'), ('alb', 'Albania'), ('dza', 'Algeria'), ('and', 'Andorra'), ('ago', 'Angola'), ('atg', 'Antigua and Barbuda'), ('arg', 'Argentina'), ('arm', 'Armenia'), ('aus', 'Australia'), ('aut', 'Austria'), ('aze', 'Azerbaijan'), ('bhs', 'Bahamas'), ('bhr', 'Bahrain'), ('bgd', 'Bangladesh'), ('brb', 'Barbados'), ('blr', 'Belarus'), ('bel', 'Belgium'), ('blz', 'Belize'), ('ben', 'Benin'), ('btn', 'Bhutan'), ('bol', 'Bolivia (Plurinational State of)'), ('bih', 'Bosnia and Herzegovina'), ('bwa', 'Botswana'), ('bra', 'Brazil'), ('brn', 'Brunei Darussalam'), ('bgr', 'Bulgaria'), ('bfa', 'Burkina Faso'), ('bdi', 'Burundi'), ('cpv', 'Cabo Verde'), ('khm', 'Cambodia'), ('cmr', 'Cameroon'), ('can', 'Canada'), ('caf', 'Central African Republic'), ('tcd', 'Chad'), ('chl', 'Chile'), ('chn', 'China'), ('col', 'Colombia'), ('com', 'Comoros'), ('cog', 'Congo'), ('cod', 'Congo, Democratic Republic of the'), ('cri', 'Costa Rica'), ('civ', "CÃ´te d'Ivoire"), ('hrv', 'Croatia'), ('cub', 'Cuba'), ('cyp', 'Cyprus'), ('cze', 'Czechia'), ('dnk', 'Denmark'), ('dji', 'Djibouti'), ('dma', 'Dominica'), ('dom', 'Dominican Republic'), ('ecu', 'Ecuador'), ('egy', 'Egypt'), ('slv', 'El Salvador'), ('gnq', 'Equatorial Guinea'), ('eri', 'Eritrea'), ('est', 'Estonia'), ('swz', 'Eswatini'), ('eth', 'Ethiopia'), ('fji', 'Fiji'), ('fin', 'Finland'), ('fra', 'France'), ('gab', 'Gabon'), ('gmb', 'Gambia'), ('geo', 'Georgia'), ('deu', 'Germany'), ('gha', 'Ghana'), ('grc', 'Greece'), ('grd', 'Grenada'), ('gtm', 'Guatemala'), ('gin', 'Guinea'), ('gnb', 'Guinea-Bissau'), ('guy', 'Guyana'), ('hti', 'Haiti'), ('hnd', 'Honduras'), ('hun', 'Hungary'), ('isl', 'Iceland'), ('ind', 'India'), ('idn', 'Indonesia'), ('irn', 'Iran (Islamic Republic of)'), ('irq', 'Iraq'), ('irl', 'Ireland'), ('isr', 'Israel'), ('ita', 'Italy'), ('jam', 'Jamaica'), ('jpn', 'Japan'), ('jor', 'Jordan'), ('kaz', 'Kazakhstan'), ('ken', 'Kenya'), ('kir', 'Kiribati'), ('prk', "Korea (Democratic People's Republic of)"), ('kor', 'Korea, Republic of'), ('kwt', 'Kuwait'), ('kgz', 'Kyrgyzstan'), ('lao', "Lao People's Democratic Republic"), ('lva', 'Latvia'), ('lbn', 'Lebanon'), ('lso', 'Lesotho'), ('lbr', 'Liberia'), ('lby', 'Libya'), ('lie', 'Liechtenstein'), ('ltu', 'Lithuania'), ('lux', 'Luxembourg'), ('mdg', 'Madagascar'), ('mwi', 'Malawi'), ('mys', 'Malaysia'), ('mdv', 'Maldives'), ('mli', 'Mali'), ('mlt', 'Malta'), ('mhl', 'Marshall Islands'), ('mrt', 'Mauritania'), ('mus', 'Mauritius'), ('mex', 'Mexico'), ('fsm', 'Micronesia (Federated States of)'), ('mda', 'Moldova, Republic of'), ('mco', 'Monaco'), ('mng', 'Mongolia'), ('mne', 'Montenegro'), ('mar', 'Morocco'), ('moz', 'Mozambique'), ('mmr', 'Myanmar'), ('nam', 'Namibia'), ('nru', 'Nauru'), ('npl', 'Nepal'), ('nld', 'Netherlands'), ('nzl', 'New Zealand'), ('nic', 'Nicaragua'), ('ner', 'Niger'), ('nga', 'Nigeria'), ('mkd', 'North Macedonia'), ('nor', 'Norway'), ('omn', 'Oman'), ('pak', 'Pakistan'), ('plw', 'Palau'), ('pan', 'Panama'), ('png', 'Papua New Guinea'), ('pry', 'Paraguay'), ('per', 'Peru'), ('phl', 'Philippines'), ('pol', 'Poland'), ('prt', 'Portugal'), ('qat', 'Qatar'), ('rou', 'Romania'), ('rus', 'Russian Federation'), ('rwa', 'Rwanda'), ('kna', 'Saint Kitts and Nevis'), ('lca', 'Saint Lucia'), ('vct', 'Saint Vincent and the Grenadines'), ('wsm', 'Samoa'), ('smr', 'San Marino'), ('stp', 'Sao Tome and Principe'), ('sau', 'Saudi Arabia'), ('sen', 'Senegal'), ('srb', 'Serbia'), ('syc', 'Seychelles'), ('sle', 'Sierra Leone'), ('sgp', 'Singapore'), ('svk', 'Slovakia'), ('svn', 'Slovenia'), ('slb', 'Solomon Islands'), ('som', 'Somalia'), ('zaf', 'South Africa'), ('ssd', 'South Sudan'), ('esp', 'Spain'), ('lka', 'Sri Lanka'), ('sdn', 'Sudan'), ('sur', 'Suriname'), ('swe', 'Sweden'), ('che', 'Switzerland'), ('syr', 'Syrian Arab Republic'), ('tjk', 'Tajikistan'), ('tza', 'Tanzania, United Republic of'), ('tha', 'Thailand'), ('tls', 'Timor-Leste'), ('tgo', 'Togo'), ('ton', 'Tonga'), ('tto', 'Trinidad and Tobago'), ('tun', 'Tunisia'), ('tur', 'Turkey'), ('tkm', 'Turkmenistan'), ('tuv', 'Tuvalu'), ('uga', 'Uganda'), ('ukr', 'Ukraine'), ('are', 'United Arab Emirates'), ('gbr', 'United Kingdom of Great Britain and Northern Ireland'), ('usa', 'United States of America'), ('ury', 'Uruguay'), ('uzb', 'Uzbekistan'), ('vut', 'Vanuatu'), ('ven', 'Venezuela (Bolivarian Republic of)'), ('vnm', 'Viet Nam'), ('yem', 'Yemen'), ('zmb', 'Zambia'), ('zwe', 'Zimbabwe')], max_length=60)),
                ('likes', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, upload_to=rango.models.recipe_image_dir)),
                ('name', models.CharField(max_length=100)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=rango.models.user_image_dir)),
                ('favourites', models.ManyToManyField(blank=True, to='rango.Recipe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.UserProfile'),
        ),
    ]
