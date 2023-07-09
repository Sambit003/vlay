import pynecone as pc

class VlayConfig(pc.Config):
    pass

config = VlayConfig(
    app_name="vlay",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)