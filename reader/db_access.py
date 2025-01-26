from parliament import Sitzung, Redner
from db_config import getDBUrl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collections import Counter

def store_sitzung_bulk(sitzung, session):
    # Collect all redner_ids from the Sitzung's Reden
    redner_ids = {rede.redner.redner_id for rede in sitzung.reden}
    
    # Query for all existing Redner in the database that match these redner_ids
    existing_redners = session.query(Redner).filter(Redner.redner_id.in_(redner_ids)).all()
    
    # Map existing Redner by their redner_id for fast lookup
    redner_cache = {redner.redner_id: redner for redner in existing_redners}
    
    # List to hold any new Redner that need to be added
    new_redners = []
    
    # Check each Rede to ensure the associated Redner exists
    for rede in sitzung.reden:
        redner_id = rede.redner.redner_id
        
        if redner_id not in redner_cache:
            # If the Redner does not exist in the cache, add it to the list of new Redner
            new_redners.append(rede.redner)
            redner_cache[redner_id] = rede.redner  # Cache the new Redner

        # Assign the Redner to the Rede (either new or existing)
        rede.redner = redner_cache[redner_id]
    
    # Add all new Redner to the session in bulk
    if new_redners:
        session.add_all(new_redners)
    
    # Add the Sitzung to the session
    session.add(sitzung)
    
    # Commit all changes at once
    session.commit()



def store_sitzung(sitzung: Sitzung):
    # Set up engine and session
    engine = create_engine(getDBUrl())
    Session = sessionmaker(bind=engine)
    session = Session()
    store_sitzung_bulk(sitzung, session)

    # # Example: Creating a Sitzung with related objects
    # try:
    #     # Add the Sitzung object to the session
    #     session.add(sitzung)

    #     # Commit the transaction
    #     session.commit()
    #     print("Sitzung and related objects saved successfully!")
    # except Exception as e:
    #     session.rollback()  # Rollback if there is an error
    #     print(f"Error saving Sitzung: {e}")
    # finally:
    #     session.close()
