from odoo import models, fields, api


class GrantAiAssistant(models.Model):
    _name = 'grant.ai.assistant'
    _description = 'AI Grant Assistant'

    name = fields.Char("Assistant Name", required=True)
    user_input = fields.Text("User Input")
    ai_response = fields.Text("AI Response")

    @api.model
    def generate_response(self, user_input):
        # Basic rule-based AI response
        if "funding" in user_input:
            return "We suggest focusing on grants related to technology and innovation."
        elif "geographic area" in user_input:
            return "Consider targeting regions with a high need for development, such as rural areas."
        else:
            return "Please provide more details for a tailored suggestion."
