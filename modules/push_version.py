from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.auth import get_auth
from modules.core.http_status import handle


def push_version(package):
    print(
        (lambda code: f"Success, users will receive message to update {package}" if code in [200, 201]
         else "Error happened")(handle(
            request.post(f"{horsy_vars.url}/packages/push-version",
                         json={
                             'auth': get_auth(),
                             'name': package
                         }
                         ).status_code
        )[1])
    )
