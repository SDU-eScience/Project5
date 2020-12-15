Summary Table
=============

.. raw:: html
    
    <style>
        table.docutils td p {
         font-size: 0.85em !important;
        }
    </style>


.. table::
    :align: left

    +-------------------+------------+-------------+--------------------------+--------------------------+--------------------------+-------------------------+-------------+
    |                   |        DeiC Type 1       |                            DeiC Type 2                                         | Deic Type 3             | DeiC Type 4 |
    +===================+============+=============+==========================+==========================+==========================+=========================+=============+
    |                   | AAU        | SDU         |  GenomeDK                | Computerome2             |  Sophia                  | SDU                     | KU          |
    +-------------------+------------+-------------+--------------------------+--------------------------+--------------------------+-------------------------+-------------+
    |User Management    | AD         | UCloud      |  NIS/Local Unix Users    | Local Users/LDAP/2FA     |  AD                      | IPA                     | TBD         |
    +-------------------+------------+-------------+--------------------------+--------------------------+--------------------------+-------------------------+-------------+
    |Storage Systems    | CEPH       | CephFS/GPFS |  BeeGFS                  | OneFS                    |  BeeGFS/CEPH             | GPFS                    | TBD         |
    +-------------------+------------+-------------+--------------------------+--------------------------+--------------------------+-------------------------+-------------+
    |Job Management     | OpenStack  | UCloud      |  Slurm                   | Moab                     |  Slurm                   | Slurm                   | TBD         |
    +-------------------+------------+-------------+--------------------------+--------------------------+--------------------------+-------------------------+-------------+
    |Project Management | OpenStack  | UCloud      |  Slurm + custom scripts  | Moab accounting manager  |  Slurm + custom scripts  | Slurm + custom scripts  | TBD         |
    +-------------------+------------+-------------+--------------------------+--------------------------+--------------------------+-------------------------+-------------+


.. raw:: html

    <script
        type="text/javascript"
        src="https://utteranc.es/client.js"
        async="async"
        repo="emolinaro/deic-project5"
        issue-term="pathname"
        theme="github-light"
        label="💬 comment"
        crossorigin="anonymous"
    />
