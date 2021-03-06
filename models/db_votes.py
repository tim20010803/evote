NE = IS_NOT_EMPTY()

maybe_can_choose = AS_SERVICE or DEVELOPMENT

# auth.settings.extra_fields['auth_user'] = [
#     Field('is_manager','boolean',default=True, writable=maybe_can_choose, readable=maybe_can_choose)]

auth.define_tables(username=False, signature=False)

db.define_table(
    'election',
    Field('title',requires=NE),
    Field('ballot_model','text',requires=NE), # empty ballot
    Field('voters','upload',requires=NE,autodelete=True),
    Field('manager','text',requires=NE,writable=False),
    Field('deadline','datetime'),
    Field('comments_vote_email','text'),
    Field('comments_voted_email','text'),
    Field('comments_not_voted_email','text'),
    Field('email_sender',requires=IS_EMAIL(),default=mail.settings.sender,writable=False),
    Field('public_key','text',writable=False,readable=False),
    Field('private_key','text',writable=False,readable=False),
    Field('counters','json',writable=False,readable=False),
    Field('closed','boolean',writable=False,readable=False),
    Field('started','boolean',writable=False,readable=False),
    auth.signature,
    format='%(title)s')

db.define_table(
    'voter',
    Field('voter_uuid',writable=False,readable=False),
    Field('election_id',db.election,writable=False),
    Field('email',requires=IS_EMAIL()),
    Field('voted','boolean',default=False),
    Field('invited_on','datetime'))

db.define_table(
    'ballot',
    Field('election_id',db.election),
    Field('ballot_content','text'),  # voted or blank ballot
    Field('voted','boolean',default=False),
    Field('voted_on','datetime',default=None),
    Field('results','json',default={}),
    Field('ballot_uuid'), # uuid embedded in ballot
    Field('signature')) # signature of ballot (voted or blank)
