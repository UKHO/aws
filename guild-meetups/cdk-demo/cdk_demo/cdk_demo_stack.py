from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as lam,
    aws_lambda_event_sources as lam_events,
    aws_iam as iam,
    core,
)


class CdkDemoStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "BucketOne", bucket_name="jc-100-test-bucket")

        another_bucket = s3.Bucket(self, "BucketTwo", bucket_name="jc-200-test-bucket")

        lambda_function = lam.Function(
            self,
            "test-copy-bucket-cdk",
            runtime=lam.Runtime.PYTHON_3_7,
            events=[
                lam_events.S3EventSource(
                    bucket,
                    events=[
                        s3.EventType.OBJECT_CREATED_PUT,
                        s3.EventType.OBJECT_CREATED_COPY,
                    ],
                )
            ],
            handler="index.handle",
            code=lam.Code.from_asset("lambda"),
            environment={"DESTINATION_BUCKET": another_bucket.bucket_name},
            initial_policy=[
                iam.PolicyStatement(
                    actions=["s3:PutObject", "s3:GetObject"],
                    resources=[
                        bucket.bucket_arn,
                        bucket.arn_for_objects("*"),
                        another_bucket.bucket_arn,
                        another_bucket.arn_for_objects("*"),
                    ],
                )
            ],
        )
