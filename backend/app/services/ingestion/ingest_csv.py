'''
Docstring for ingest_csv file
'''

import csv
from datetime import datetime

from app.db.session import SessionLocal
from app.models.sales import IngestionRun, IngestionStatus, SalesOrder


def ingest_csv(file_path):
    db = SessionLocal()

    # Create ingestion run
    run = IngestionRun(
        source = "manual",
        file_path = file_path,
        status = IngestionStatus.UPLOADED,
    )

    db.add(run)
    db.flush()

    try:
        with open(file_path) as file:
            reader = csv.DictReader(file)

            # Check Headers
            required = {'occurred_at','order_id','total'}
            headers = set(reader.fieldnames) if reader.fieldnames else set()
            missing = required - headers

            if missing:
                raise ValueError(f"Missing columns: {missing}")

            for row in reader:
                validated = validate_row(row)

                order = SalesOrder(
                    ingestion_run_id = run.id,
                    **validated
                )
                db.add(order)

            run.status = IngestionStatus.PROCESSED
            db.commit()
            print("Success!")

    except Exception as e:
        run.status = IngestionStatus.FAILED
        db.rollback()
        print(f"Failed: {e}")
        raise
    finally:
        db.close()


"""
Helper function for ingest_csv
"""
def validate_row(row):
    # Check id
    if not row['order_id'].strip():
        raise ValueError("order_id is null")

    # Check total
    try:
        total = float(row['total'])
        if total < 0:
            raise ValueError("Total is less than 0")
    except Exception as err:
        raise ValueError(f"Invalid total: {row['total']}") from err

    # Check date
    date_string = row['occurred_at']
    parsed_date = None
    formats = [
        '%m-%d-%Y',
        '%Y-%m-%d %H:%M:%S',
        '%d-%m-%Y',
    ]

    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_string, fmt)
            break
        except ValueError:
            continue
    if parsed_date is None:
        raise ValueError(f"Cannot parse date: {date_string}")
    return {
        'order_id': row['order_id'].strip(),
        'total': total,
        'occurred_at': parsed_date,
    }



