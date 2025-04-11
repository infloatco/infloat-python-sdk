# Reference
<details><summary><code>client.<a href="src/Infloat/client.py">register_user_auth_register_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.register_user_auth_register_post(
    name="name",
    email="email",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">login_auth_login_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.login_auth_login_post(
    email="email",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_user_me_auth_me_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_user_me_auth_me_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_projects_projects_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_projects_projects_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**skip:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">create_project_projects_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.create_project_projects_post(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_project_projects_project_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_project_projects_project_id_get(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_models_projects_project_id_models_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_models_projects_project_id_models_get(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">upload_model_projects_project_id_models_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.upload_model_projects_project_id_models_post(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**model_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_clients_projects_project_id_clients_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_clients_projects_project_id_clients_get(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">register_client_projects_project_id_clients_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.register_client_projects_project_id_clients_post(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_client_config_client_config_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_client_config_client_config_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_trainings_projects_project_id_trainings_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_trainings_projects_project_id_trainings_get(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">start_training_projects_project_id_trainings_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.start_training_projects_project_id_trainings_post(
    project_id="project_id",
    model_id="model_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_rounds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**min_clients:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_clients:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**aggregation_strategy:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_training_status_trainings_training_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_training_status_trainings_training_id_get(
    training_id="training_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**training_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">get_training_results_trainings_training_id_results_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.get_training_results_trainings_training_id_results_get(
    training_id="training_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**training_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**round_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">submit_metrics_client_submit_metrics_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.submit_metrics_client_submit_metrics_post(
    client_id="client_id",
    round=1,
    loss=1.1,
    accuracy=1.1,
    training_samples=1,
    training_time=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**round:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**loss:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**accuracy:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**training_samples:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**training_time:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_metrics:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/Infloat/client.py">health_check_health_get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from Infloat import InfloatApi

client = InfloatApi(
    base_url="https://yourhost.com/path/to/api",
)
client.health_check_health_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

