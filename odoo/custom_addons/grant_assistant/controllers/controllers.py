from odoo import http
from odoo.http import request

class GrantAssistantController(http.Controller):

    @http.route('/grant/assistant', auth='user', methods=['POST'], csrf=False)
    def ai_assistant(self, **kwargs):
        user_input = kwargs.get('user_input')
        assistant = request.env['grant.assistant'].create({'name': 'Grant Assistant', 'user_input': user_input})
        ai_response = assistant.generate_response(user_input)
        return {'response': ai_response}
