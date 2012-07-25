#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import datetime
from decimal import Decimal
from trytond.model import ModelSQL, fields
from trytond.pyson import Eval


class Boolean(ModelSQL):
    'Boolean'
    _name = 'test.boolean'
    _description = __doc__
    boolean = fields.Boolean(string='Boolean', help='Test boolean')

Boolean()


class BooleanDefault(ModelSQL):
    'Boolean Default'
    _name = 'test.boolean_default'
    _description = __doc__
    boolean = fields.Boolean(string='Boolean', help='Test boolean')

    def default_boolean(self):
        return True

BooleanDefault()


class Integer(ModelSQL):
    'Integer'
    _name = 'test.integer'
    _description = __doc__
    integer = fields.Integer(string='Integer', help='Test integer',
            required=False)

Integer()


class IntegerDefault(ModelSQL):
    'Integer Default'
    _name = 'test.integer_default'
    _description = __doc__
    integer = fields.Integer(string='Integer', help='Test integer',
            required=False)

    def default_integer(self):
        return 5

IntegerDefault()


class IntegerRequired(ModelSQL):
    'Integer Required'
    _name = 'test.integer_required'
    _description = __doc__
    integer = fields.Integer(string='Integer', help='Test integer',
            required=True)

IntegerRequired()


class Float(ModelSQL):
    'Float'
    _name = 'test.float'
    _description = __doc__
    float = fields.Float(string='Float', help='Test float',
            required=False)

Float()


class FloatDefault(ModelSQL):
    'Float Default'
    _name = 'test.float_default'
    _description = __doc__
    float = fields.Float(string='Float', help='Test float',
            required=False)

    def default_float(self):
        return 5.5

FloatDefault()


class FloatRequired(ModelSQL):
    'Float Required'
    _name = 'test.float_required'
    _description = __doc__
    float = fields.Float(string='Float', help='Test float',
            required=True)

FloatRequired()


class FloatDigits(ModelSQL):
    'Float Digits'
    _name = 'test.float_digits'
    _description = __doc__
    digits = fields.Integer('Digits')
    float = fields.Float(string='Float', help='Test float',
        required=False, digits=(16, Eval('digits', 2)),
        depends=['digits'])

FloatDigits()


class Numeric(ModelSQL):
    'Numeric'
    _name = 'test.numeric'
    _description = __doc__
    numeric = fields.Numeric(string='Numeric', help='Test numeric',
            required=False)

Numeric()


class NumericDefault(ModelSQL):
    'Numeric Default'
    _name = 'test.numeric_default'
    _description = __doc__
    numeric = fields.Numeric(string='Numeric', help='Test numeric',
            required=False)

    def default_numeric(self):
        return Decimal('5.5')

NumericDefault()


class NumericRequired(ModelSQL):
    'Numeric Required'
    _name = 'test.numeric_required'
    _description = __doc__
    numeric = fields.Numeric(string='Numeric', help='Test numeric',
            required=True)

NumericRequired()


class NumericDigits(ModelSQL):
    'Numeric Digits'
    _name = 'test.numeric_digits'
    _description = __doc__
    digits = fields.Integer('Digits')
    numeric = fields.Numeric(string='Numeric', help='Test numeric',
        required=False, digits=(16, Eval('digits', 2)),
        depends=['digits'])

NumericDigits()


class Char(ModelSQL):
    'Char'
    _name = 'test.char'
    _description = __doc__
    char = fields.Char(string='Char', size=None, help='Test char',
            required=False)

Char()


class CharDefault(ModelSQL):
    'Char Default'
    _name = 'test.char_default'
    _description = __doc__
    char = fields.Char(string='Char', size=None, help='Test char',
            required=False)

    def default_char(self):
        return 'Test'

CharDefault()


class CharRequired(ModelSQL):
    'Char Required'
    _name = 'test.char_required'
    _description = __doc__
    char = fields.Char(string='Char', size=None, help='Test char',
            required=True)

CharRequired()


class CharSize(ModelSQL):
    'Char Size'
    _name = 'test.char_size'
    _description = __doc__
    char = fields.Char(string='Char', size=5, help='Test char',
            required=False)

CharSize()


class CharTranslate(ModelSQL):
    'Char Translate'
    _name = 'test.char_translate'
    _description = __doc__
    char = fields.Char(string='Char', size=None, help='Test char',
            required=False, translate=True)

CharTranslate()


class Text(ModelSQL):
    'Text'
    _name = 'test.text'
    _description = __doc__
    text = fields.Text(string='Text', size=None, help='Test text',
            required=False)

Text()


class TextDefault(ModelSQL):
    'Text Default'
    _name = 'test.text_default'
    _description = __doc__
    text = fields.Text(string='Text', size=None, help='Test text',
            required=False)

    def default_text(self):
        return 'Test'

TextDefault()


class TextRequired(ModelSQL):
    'Text Required'
    _name = 'test.text_required'
    _description = __doc__
    text = fields.Text(string='Text', size=None, help='Test text',
            required=True)

TextRequired()


class TextSize(ModelSQL):
    'Text Size'
    _name = 'test.text_size'
    _description = __doc__
    text = fields.Text(string='Text', size=5, help='Test text',
            required=False)

TextSize()


class TextTranslate(ModelSQL):
    'Text Translate'
    _name = 'test.text_translate'
    _description = __doc__
    text = fields.Text(string='Text', size=None, help='Test text',
            required=False, translate=True)

TextTranslate()


class Sha(ModelSQL):
    'Sha'
    _name = 'test.sha'
    _description = __doc__
    sha = fields.Sha(string='Sha', help='Test sha',
            required=False)

Sha()


class ShaDefault(ModelSQL):
    'Sha Default'
    _name = 'test.sha_default'
    _description = __doc__
    sha = fields.Sha(string='Sha', help='Test sha',
            required=False)

    def default_sha(self):
        return 'Sha'

ShaDefault()


class ShaRequired(ModelSQL):
    'Sha Required'
    _name = 'test.sha_required'
    _description = __doc__
    sha = fields.Sha(string='Sha', help='Test sha',
            required=True)

ShaRequired()


class Date(ModelSQL):
    'Date'
    _name = 'test.date'
    _description = __doc__
    date = fields.Date(string='Date', help='Test date',
            required=False)

Date()


class DateDefault(ModelSQL):
    'Date Default'
    _name = 'test.date_default'
    _description = __doc__
    date = fields.Date(string='Date', help='Test date',
            required=False)

    def default_date(self):
        return datetime.date(2000, 1, 1)

DateDefault()


class DateRequired(ModelSQL):
    'Date Required'
    _name = 'test.date_required'
    _description = __doc__
    date = fields.Date(string='Date', help='Test date',
            required=True)

DateRequired()


class DateTime(ModelSQL):
    'DateTime'
    _name = 'test.datetime'
    _description = __doc__
    datetime = fields.DateTime(string='DateTime', help='Test datetime',
            required=False)

DateTime()


class DateTimeDefault(ModelSQL):
    'DateTime Default'
    _name = 'test.datetime_default'
    _description = __doc__
    datetime = fields.DateTime(string='DateTime', help='Test datetime',
            required=False)

    def default_datetime(self):
        return datetime.datetime(2000, 1, 1, 12, 0, 0, 0)

DateTimeDefault()


class DateTimeRequired(ModelSQL):
    'DateTime Required'
    _name = 'test.datetime_required'
    _description = __doc__
    datetime = fields.DateTime(string='DateTime', help='Test datetime',
            required=True)

DateTimeRequired()


class DateTimeFormat(ModelSQL):
    'DateTime Format'
    _name = 'test.datetime_format'
    _description = __doc__
    datetime = fields.DateTime(string='DateTime', format='%H:%M')

DateTimeFormat()


class Time(ModelSQL):
    'Time'
    _name = 'test.time'
    _description = __doc__
    time = fields.Time(string='Time', help='Test time', required=False)

Time()


class TimeDefault(ModelSQL):
    'Time Default'
    _name = 'test.time_default'
    _description = __doc__
    time = fields.Time(string='Time', help='Test time', required=False)

    def default_time(self):
        return datetime.time(16, 30)

TimeDefault()


class TimeRequired(ModelSQL):
    'Time'
    _name = 'test.time_required'
    _description = __doc__
    time = fields.Time(string='Time', help='Test time', required=True)

TimeRequired()


class TimeFormat(ModelSQL):
    'Time Format'
    _name = 'test.time_format'
    _description = __doc__
    time = fields.Time(string='Time', format='%H:%M')

TimeFormat()


class One2One(ModelSQL):
    'One2One'
    _name = 'test.one2one'
    _description = __doc__
    name = fields.Char('Name', required=True)
    one2one = fields.One2One('test.one2one.relation', 'origin', 'target',
            string='One2One', help='Test one2one', required=False)

One2One()


class One2OneTarget(ModelSQL):
    'One2One Target'
    _name = 'test.one2one.target'
    name = fields.Char('Name', required=True)

One2OneTarget()


class One2OneRelation(ModelSQL):
    'One2One Relation'
    _name = 'test.one2one.relation'
    _description = __doc__
    origin = fields.Many2One('test.one2one', 'Origin')
    target = fields.Many2One('test.one2one.target', 'Target')

    def __init__(self):
        super(One2OneRelation, self).__init__()
        self._sql_constraints += [
            ('origin_unique', 'UNIQUE(origin)',
                'Origin must be unique'),
            ('target_unique', 'UNIQUE(target)',
                'Target must be unique'),
        ]

One2OneRelation()


class One2OneRequired(ModelSQL):
    'One2One'
    _name = 'test.one2one_required'
    _description = __doc__
    name = fields.Char('Name', required=True)
    one2one = fields.One2One('test.one2one_required.relation', 'origin',
        'target', string='One2One', help='Test one2one', required=True)

One2OneRequired()


class One2OneRequiredRelation(ModelSQL):
    'One2One Relation'
    _name = 'test.one2one_required.relation'
    _description = __doc__
    origin = fields.Many2One('test.one2one_required', 'Origin')
    target = fields.Many2One('test.one2one.target', 'Target')

    def __init__(self):
        super(One2OneRequiredRelation, self).__init__()
        self._sql_constraints += [
            ('origin_unique', 'UNIQUE(origin)',
                'Origin must be unique'),
            ('target_unique', 'UNIQUE(target)',
                'Target must be unique'),
        ]

One2OneRequiredRelation()


class One2Many(ModelSQL):
    'One2Many Relation'
    _name = 'test.one2many'
    _description = __doc__
    name = fields.Char('Name', required=True)
    targets = fields.One2Many('test.one2many.target', 'origin', 'Targets')

One2Many()


class One2ManyTarget(ModelSQL):
    'One2Many Target'
    _name = 'test.one2many.target'
    _description = __doc__
    name = fields.Char('Name', required=True)
    origin = fields.Many2One('test.one2many', 'Origin')

One2ManyTarget()


class One2ManyRequired(ModelSQL):
    'One2Many Required'
    _name = 'test.one2many_required'
    _description = __doc__
    name = fields.Char('Name', required=True)
    targets = fields.One2Many('test.one2many_required.target', 'origin',
        'Targets', required=True)

One2ManyRequired()


class One2ManyRequiredTarget(ModelSQL):
    'One2Many Required Target'
    _name = 'test.one2many_required.target'
    _description = __doc__
    name = fields.Char('Name', required=True)
    origin = fields.Many2One('test.one2many_required', 'Origin')

One2ManyRequiredTarget()


class One2ManyReference(ModelSQL):
    'One2Many Reference Relation'
    _name = 'test.one2many_reference'
    _description = __doc__
    name = fields.Char('Name', required=True)
    targets = fields.One2Many('test.one2many_reference.target', 'origin',
        'Targets')

One2ManyReference()


class One2ManyReferenceTarget(ModelSQL):
    'One2Many Reference Target'
    _name = 'test.one2many_reference.target'
    _description = __doc__
    name = fields.Char('Name', required=True)
    origin = fields.Reference('Origin', [
            ('test.one2many_reference', 'One2Many Reference'),
            ])

One2ManyReferenceTarget()


class One2ManySize(ModelSQL):
    'One2Many Size Relation'
    _name = 'test.one2many_size'
    _description = __doc__
    targets = fields.One2Many('test.one2many_size.target', 'origin', 'Targets',
        size=3)

One2ManySize()


class One2ManySizeTarget(ModelSQL):
    'One2Many Size Target'
    _name = 'test.one2many_size.target'
    _description = __doc__
    origin = fields.Many2One('test.one2many_size', 'Origin')

One2ManySizeTarget()


class One2ManySizePYSON(ModelSQL):
    'One2Many Size PYSON Relation'
    _name = 'test.one2many_size_pyson'
    _description = __doc__
    limit = fields.Integer('Limit')
    targets = fields.One2Many('test.one2many_size_pyson.target', 'origin',
        'Targets', size=Eval('limit', 0))

One2ManySizePYSON()


class One2ManySizePYSONTarget(ModelSQL):
    'One2Many Size PYSON Target'
    _name = 'test.one2many_size_pyson.target'
    _description = __doc__
    origin = fields.Many2One('test.one2many_size_pyson', 'Origin')

One2ManySizePYSONTarget()


class Many2Many(ModelSQL):
    'Many2Many'
    _name = 'test.many2many'
    _description = __doc__
    name = fields.Char('Name', required=True)
    targets = fields.Many2Many('test.many2many.relation', 'origin', 'target',
        'Targets')

Many2Many()


class Many2ManyTarget(ModelSQL):
    'Many2Many Target'
    _name = 'test.many2many.target'
    _description = __doc__
    name = fields.Char('Name', required=True)


Many2ManyTarget()


class Many2ManyRelation(ModelSQL):
    'Many2Many Relation'
    _name = 'test.many2many.relation'
    _description = __doc__
    origin = fields.Many2One('test.many2many', 'Origin')
    target = fields.Many2One('test.many2many.target', 'Target')

Many2ManyRelation()


class Many2ManyRequired(ModelSQL):
    'Many2Many Required'
    _name = 'test.many2many_required'
    _description = __doc__
    name = fields.Char('Name', required=True)
    targets = fields.Many2Many('test.many2many_required.relation', 'origin',
        'target', 'Targets', required=True)

Many2ManyRequired()


class Many2ManyRequiredTarget(ModelSQL):
    'Many2Many Required Target'
    _name = 'test.many2many_required.target'
    _description = __doc__
    name = fields.Char('Name', required=True)


Many2ManyRequiredTarget()


class Many2ManyRequiredRelation(ModelSQL):
    'Many2Many Required Relation'
    _name = 'test.many2many_required.relation'
    _description = __doc__
    origin = fields.Many2One('test.many2many_required', 'Origin')
    target = fields.Many2One('test.many2many_required.target', 'Target')

Many2ManyRequiredRelation()


class Many2ManyReference(ModelSQL):
    'Many2Many Reference'
    _name = 'test.many2many_reference'
    _description = __doc__
    name = fields.Char('Name', required=True)
    targets = fields.Many2Many('test.many2many_reference.relation', 'origin',
        'target', 'Targets')

Many2ManyReference()


class Many2ManyReferenceTarget(ModelSQL):
    'Many2Many Reference Target'
    _name = 'test.many2many_reference.target'
    _description = __doc__
    name = fields.Char('Name', required=True)


Many2ManyReferenceTarget()


class Many2ManyReferenceRelation(ModelSQL):
    'Many2Many Relation'
    _name = 'test.many2many_reference.relation'
    _description = __doc__
    origin = fields.Reference('Origin', [
            ('test.many2many_reference', 'Many2Many Reference'),
            ])
    target = fields.Many2One('test.many2many_reference.target',
        'Reference Target')

Many2ManyReferenceRelation()


class Many2ManySize(ModelSQL):
    'Many2Many Size Relation'
    _name = 'test.many2many_size'
    _description = __doc__
    targets = fields.Many2Many('test.many2many_size.relation', 'origin',
        'target', 'Targets', size=5)

Many2ManySize()


class Many2ManySizeTarget(ModelSQL):
    'Many2Many Size Target'
    _name = 'test.many2many_size.target'
    _description = __doc__
    name = fields.Char('Name')

Many2ManySizeTarget()


class Many2ManySizeRelation(ModelSQL):
    'Many2Many Size Relation'
    _name = 'test.many2many_size.relation'
    _description = __doc__
    origin = fields.Many2One('test.many2many_size', 'Origin')
    target = fields.Many2One('test.many2many_size.target', 'Target')

Many2ManySizeRelation()


class Reference(ModelSQL):
    'Reference'
    _name = 'test.reference'
    _description = __doc__
    name = fields.Char('Name', required=True)
    reference = fields.Reference('Reference', selection=[
            ('test.reference.target', 'Target'),
            ])

Reference()


class ReferenceTarget(ModelSQL):
    'Reference Target'
    _name = 'test.reference.target'
    _description = __doc__
    name = fields.Char('Name', required=True)

ReferenceTarget()


class ReferenceRequired(ModelSQL):
    'Reference Required'
    _name = 'test.reference_required'
    _description = __doc__
    name = fields.Char('Name', required=True)
    reference = fields.Reference('Reference', selection=[
            ('test.reference.target', 'Target'),
            ])

ReferenceRequired()


class Property(ModelSQL):
    'Property'
    _name = 'test.property'
    _description = __doc__

    char = fields.Property(fields.Char('Test Char'))
    many2one = fields.Property(fields.Many2One('test.char',
            'Test Many2One'))
    numeric = fields.Property(fields.Numeric('Test Numeric'))
    selection = fields.Property(fields.Selection([
                ('option_a', 'Option A'),
                ('option_b', 'Option B')
            ], 'Test Selection'))

Property()
