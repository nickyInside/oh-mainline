# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'RepositoryCommitter', fields ['project', 'data_import_attempt']
        db.delete_unique(u'profile_repositorycommitter', ['project_id', 'data_import_attempt_id'])

        # Deleting model 'DataImportAttempt'
        db.delete_table(u'profile_dataimportattempt')

        # Deleting field 'Citation.data_import_attempt'
        db.delete_column(u'profile_citation', 'data_import_attempt_id')

        # Deleting field 'RepositoryCommitter.data_import_attempt'
        db.delete_column(u'profile_repositorycommitter', 'data_import_attempt_id')


    def backwards(self, orm):
        # Adding model 'DataImportAttempt'
        db.create_table(u'profile_dataimportattempt', (
            ('failed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profile.Person'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('web_response', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customs.WebResponse'], null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'profile', ['DataImportAttempt'])

        # Adding field 'Citation.data_import_attempt'
        db.add_column(u'profile_citation', 'data_import_attempt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profile.DataImportAttempt'], null=True),
                      keep_default=False)

        # Adding field 'RepositoryCommitter.data_import_attempt'
        db.add_column(u'profile_repositorycommitter', 'data_import_attempt',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 12, 25, 0, 0), to=orm['profile.DataImportAttempt']),
                      keep_default=False)

        # Adding unique constraint on 'RepositoryCommitter', fields ['project', 'data_import_attempt']
        db.create_unique(u'profile_repositorycommitter', ['project_id', 'data_import_attempt_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profile.citation': {
            'Meta': {'object_name': 'Citation'},
            'contributor_role': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'first_commit_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignored_due_to_duplicate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'old_summary': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True'}),
            'portfolio_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.PortfolioEntry']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'profile.forwarder': {
            'Meta': {'object_name': 'Forwarder'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'expires_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stops_being_listed_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'profile.link_person_tag': {
            'Meta': {'object_name': 'Link_Person_Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.Person']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.Tag']"})
        },
        u'profile.link_project_tag': {
            'Meta': {'object_name': 'Link_Project_Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['search.Project']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.Tag']"})
        },
        u'profile.link_sf_proj_dude_fm': {
            'Meta': {'unique_together': "[('person', 'project')]", 'object_name': 'Link_SF_Proj_Dude_FM'},
            'date_collected': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.SourceForgePerson']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.SourceForgeProject']"})
        },
        u'profile.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blacklisted_repository_committers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profile.RepositoryCommitter']", 'symmetrical': 'False'}),
            'contact_blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dont_guess_my_location': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_me_re_projects': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'expand_next_steps': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'gotten_name_from_ohloh': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'homepage_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irc_nick': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'last_polled': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '-37.3049962'}),
            'location_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_display_name': ('django.db.models.fields.CharField', [], {'default': "'Inaccessible Island'", 'max_length': '255', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '-12.6790445'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'photo_thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'photo_thumbnail_20px_wide': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'photo_thumbnail_30px_wide': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'show_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'profile.portfolioentry': {
            'Meta': {'ordering': "('-sort_order', '-id')", 'object_name': 'PortfolioEntry'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'experience_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.Person']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['search.Project']"}),
            'project_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'receive_maintainer_updates': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'use_my_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'profile.repositorycommitter': {
            'Meta': {'object_name': 'RepositoryCommitter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['search.Project']"})
        },
        u'profile.sourceforgeperson': {
            'Meta': {'object_name': 'SourceForgePerson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'profile.sourceforgeproject': {
            'Meta': {'object_name': 'SourceForgeProject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unixname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'profile.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.TagType']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'profile.tagtype': {
            'Meta': {'object_name': 'TagType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profile.unsubscribetoken': {
            'Meta': {'object_name': 'UnsubscribeToken'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profile.Person']"}),
            'string': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'search.project': {
            'Meta': {'object_name': 'Project'},
            'cached_contributor_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_icon_was_fetched_from_ohloh': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'homepage': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'icon_for_profile': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_for_search_result': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_raw': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'icon_smaller_for_badge': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'logo_contains_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'people_who_wanna_help': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects_i_wanna_help'", 'symmetrical': 'False', 'to': u"orm['profile.Person']"})
        }
    }

    complete_apps = ['profile']