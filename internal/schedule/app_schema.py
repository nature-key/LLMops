from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    query = StringField("query",
                        validators=[DataRequired(message="用户的问题不能为空"),
                                    Length(max=500)])
