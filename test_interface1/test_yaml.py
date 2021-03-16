import yaml


def test_yaml():
    env = {
        "default": "dev",
        "abc":
            {
                "dev": "127.0.0.1",
                "test": "127.0.0.2"
            }
    }
    with open("env.yaml","w")  as f:
        yaml.safe_dump(data=env,stream=f)

