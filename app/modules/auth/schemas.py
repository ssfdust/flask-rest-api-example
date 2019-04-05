from marshmallow import Schema, fields

class MsgRetSchema(Schema):
    code = fields.Int(description="return code")
    msg = fields.String(description="message info")
