# Generated by Django 4.0.2 on 2022-02-08 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон Клиента')),
                ('phone_two', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон Клиента2')),
                ('room', models.CharField(max_length=20, verbose_name='Квартира')),
                ('floor', models.CharField(max_length=20, verbose_name='Этаж')),
                ('porch', models.CharField(blank=True, max_length=5, null=True, verbose_name='Номер подъезда')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Inquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, editable=False, max_length=40, unique=True)),
                ('barter_coefficient', models.BooleanField(default=False, verbose_name='Бартер Да/Нет')),
                ('type_production', models.CharField(max_length=100, verbose_name='Тип изделия')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('source', models.CharField(blank=True, max_length=100, null=True, verbose_name='Источник')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заявки')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения заявки')),
                ('type_pay', models.CharField(blank=True, choices=[('cash', 'Оплата наличными'), ('card', 'Оплата картой'), ('installment', 'Рассрочка'), ('perechislenie', 'Перечисление')], max_length=30, null=True, verbose_name='Способ оплаты')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Итоговая стоимость')),
                ('total_white_goods', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('pay', 'Оплатились'), ('think', 'Думают'), ('not_pay', 'Отказались'), ('canceled', 'Отменен'), ('repeat', 'Повторная встреча')], max_length=50, verbose_name='Статус')),
                ('in_work', models.BooleanField(default=False, verbose_name='Если нужно зафиксировать продажу, но позже ещё прикрепить файлы')),
                ('history', models.TextField(default={})),
                ('dubl', models.BooleanField(blank=True, default=False, null=True)),
                ('derivative', models.BooleanField(blank=True, default=False, null=True)),
                ('ko_tz_archived', models.BooleanField(default=False)),
                ('to_1c', models.BooleanField(default=False)),
                ('ko_tz_status', models.PositiveSmallIntegerField(choices=[(0, 'Записи на ТЗ еще не было (либо эта заявка создана до введения нового функционала)'), (5, 'Перед ТЗ (ответств.дизайнер, КО ожидает ответа от дизайнера)'), (10, 'Перед ТЗ (ответств.КО, ТЗ ожидает ответа от КО)'), (15, 'Принят КО (ответств.ТЗ, КО ожидает ответа от ТЗ)'), (20, 'После ТЗ (ответств.КО, дизайнер ожидает ответа от КО)'), (25, 'После ТЗ (ответств.дизайнер, КО ожидает ответа от дизайнера)'), (30, 'На проверке (ответств.КО, дизайнер ожидает ответа от КО)'), (35, 'Возврат (ответств.дизайнер, КО ожидает от дизайнера исправлений)'), (40, 'Принято (ответств.дизайнер, ожидается оплата от клиента и подтверждение от дизайнера)'), (45, 'На сдачу в работу | Оплаченные (ответств.дизайнер, КО ожидает ответа от дизайнера)'), (50, 'Сданные в работу | Договор на проверке (ответств.КО, от КО ожидается подтверждение)'), (55, 'Требующие корректировки (ответств.дизайнер, КО ожидает от дизайнера корректировок)'), (60, 'Повторный замер с дог. (кол должны записать на ТЗ)'), (65, 'Повторный замер с дог. (ответств.ТЗ, КО ожидает ответа от ТЗ)'), (70, 'После повторного ТЗ (ответств.КО, дизайнер ожидает от КО проверки)'), (75, 'Договор в работе'), (80, 'Отмененные ТЗ. КО проверяет, почему ТЗ был удален (кроме "отмененных" и "отказавшихся")')], default=0)),
                ('ko_tz_route', models.PositiveSmallIntegerField(choices=[(0, 'Маршрут заявки не выбран')], default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inquery.client', verbose_name='Клиент')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquery_designer', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер/Дизайнер')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquery_owner', to=settings.AUTH_USER_MODEL, verbose_name='Создатель заявки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'permissions': (('is_designer', 'Is designer'), ('is_call_center', 'Is call-center'), ('is_chief', 'Is chief'), ('is_service', 'Is service man'), ('vozm_vystavlyat_vozmozhnosti_na_upravlenie_pravami', 'Возможность выставлять возможности на управление правами'), ('vozm_sozdavat_vsem_novye_zayavki_sobytiya_repin', 'Возможность создавать ВСЕМ ДИЗАЙНЕРАМ новые заявки/события, а также удалять любые события'), ('vozm_sozdavat_tolko_sebe_novye_zayavki_sobytiya_repin', 'Возможность создавать ТОЛЬКО СЕБЕ новые заявки/события, а также удалять свои события'), ('vozm_perenaznachat_dizajnerov_v_zayavkah', 'Возможность редактировать и удалять любые заявки и переназначать дизайнеров в заявках, ставить статус "Дубль"'), ('vozm_sozdavat_novye_tz', 'Возможность создавать новые ТЗ, редактировать и удалять существующие ТЗ'), ('vozm_zanimat_bronirovat_vremya_u_tekh_zamershchikov', 'Возможность занимать/бронировать время у тех.замерщиков, а также освобождать (удалять соотв. события) такое забронированное время'), ('vozm_sozdavat_novyh_sotrudnikov_udalyat_uvolnyat_i_peremeshchat_mezhdu_otdelami', 'Возможность создавать новых сотрудников, удалять, увольнять и перемещать между отделами, редактировать почту'), ('vozm_skachivat_vse_zayavki_v_xls', 'Возможность скачивать все заявки в XLS'), ('vozm_prosmatrivat_i_ispolzovat_stranicu_dlya_rukovoditelya_tz', 'Возможность просматривать и использовать страницу для руководителя ТЗ'), ('vozm_prosmatrivat_i_raspechatyvat_grafik_tz', 'Возможность просматривать и распечатывать график ТЗ'), ('vozm_redaktirovat_grafik_prostavlyat_vyhodnye_v_kalendare_i_v_grafike', 'Возможность редактировать график (проставлять выходные в календаре и в графике)'), ('vozm_prosmotra_grafika', 'Возможность просмотра графика'), ('vozm_prosmotra_statistiki', 'Возможность просмотра статистики'), ('vozm_prosmotra_otchetov', 'Возможность просмотра отчетов'), ('vozm_prosmatrivat_zayavki_no_ne_redaktirovat_zayavki', 'Возможность просматривать заявки (но не редактировать заявки)'), ('vozm_prosmatrivat_lyubye_zayavki_no_ne_redaktirovat_zayavki', 'Возможность просматривать ЛЮБЫЕ заявки (но не редактировать заявки)'), ('vozm_ispolzovaniya_poiska', 'Возможность использования поиска'), ('opoveshchenie_o_vhodyashchih_zvonkah_na_telefony_kol_centra', 'Оповещение о входящих звонках на телефоны кол центра'), ('vozm_skachivat_neoplachen_zayavki_v_xls', 'Возможность скачивать неоплаченные заявки в XLS')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='InqueryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_back', models.DateField(blank=True, null=True)),
                ('start_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Дата замера')),
                ('comment', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('pay', 'Оплатились'), ('think', 'Думают'), ('not_pay', 'Отказались'), ('canceled', 'Отменен'), ('repeat', 'Повторная встреча')], max_length=50, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('hidden', models.BooleanField(default=False, verbose_name='Заявка скрыта/активна')),
                ('actual', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('froze', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inquery.inquery', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Статус заявки',
                'verbose_name_plural': 'Статусы заявок',
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='InqueryFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название файла')),
                ('path', models.CharField(max_length=255, verbose_name='Путь к файлу')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('is_delete', models.BooleanField(default=False)),
                ('froze_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inquery.inquerystatus', verbose_name='Статус заявки')),
            ],
            options={
                'verbose_name': 'Файл заявки',
                'verbose_name_plural': 'Файлы заявок',
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('all_day', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('canceled', models.BooleanField(default=False)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_designer', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
        ),
    ]