from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "insurance" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(100) NOT NULL,
    "rate" DECIMAL(18,5) NOT NULL,
    "date" DATE NOT NULL,
    CONSTRAINT "uid_insurance_cargo_t_e2fe81" UNIQUE ("cargo_type", "date")
);
COMMENT ON COLUMN "insurance"."cargo_type" IS 'glass: Glass\nother: Other';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
