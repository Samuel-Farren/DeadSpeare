
export BUCKET_NAME=deadspeare
export JOB_NAME="deadSpeare_train_$(date +%Y%m%d_%H%M%S)"
export JOB_DIR=gs://$BUCKET_NAME/$JOB_NAME
export REGION=us-east1

gcloud ml-engine jobs submit training $JOB_NAME \
--job-dir gs://$BUCKET_NAME/$JOB_NAME \
--runtime-version 1.0 \
--module-name trainer.small-deadspeare \
--package-path ./trainer \
--region $REGION \
--config=trainer/cloudml-gpu.yaml \
-- \
--train-file gs://deadspeare/deadpoolLines.txt
